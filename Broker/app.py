import json
from flask import Flask, render_template, request, url_for, flash, redirect
import flask
from werkzeug.exceptions import abort
import sqlite3
import os
import logging
import jsonify
import requests

topics = ["IOT/tas", "TCD/tas", "COL/tas", "CYP/tas"]
subscribers = ["subscriber9", "subscriber10", "subscriber11", "subscriber12"]

app = Flask(__name__)

logger = logging.getLogger('werkzeug')  # grabs underlying WSGI logger
handler = logging.FileHandler('test.log')  # creates handler for the log file
logger.addHandler(handler)  # adds handler to the werkzeug WSGI logger
app.config['SECRET_KEY'] = 'abcd'


def get_db_connection():
    # print(os.getcwd())
    conn = sqlite3.connect('./data/database.db')  # link to the broker is here
    conn.row_factory = sqlite3.Row
    return conn

# @app.route('/displaypublisher', methods=('GET', 'POST'))
# def displaypublisher():
#     conn = get_db_connection(period, phen, advertise,
#                              country)  # take this from post
#     climate = conn.execute('SELECT * FROM climate').fetchall()
#     conn.close()
#     return render_template('messagereceiver.html', climate=climate)


#to call publisher function
@app.route('/pub', methods=('GET', 'POST'))
def pub():
    conn = get_db_connection()
    json_data = flask.request.json
    app.logger.info(json_data)
    publisherfunction(json_data)
    climate = conn.execute('SELECT * FROM climate').fetchall()
    # print(json_data)
    conn.close()
    # return json_data.text

#to call subscriberfunction
@app.route('/sub', methods=('GET', 'POST'))
def sub():
    conn = get_db_connection()
    json_data = flask.request.json
    app.logger.info(json_data)

    phen = json_data['PHEN']
    id = json_data['ID']
    country = json_data['COUNTRY']
    subscribe = json_data['SUBSCRIBE']

    topic = country + "/" + phen
    if topic not in topics:
        to_next_broker(json_data)
    else:
        subscriberfunction(json_data)
        climate = conn.execute('SELECT * FROM climate').fetchall()
        # print(json_data)
        conn.close()
    # return json_data.text

@app.route('/print', methods=('GET', 'POST'))
def print():
    conn = get_db_connection()
    climate = conn.execute('SELECT * FROM climate').fetchall()
    return render_template('messagereceiver.html', climate=climate)

#To call the display for subscribers
@app.route('/susbscriber_view', methods=('GET', 'POST'))
def susbscriber_view():
    json_data = flask.request.json
    id = json_data["ID"]
    # ID = str(ID)
    app.logger.info(id)
    conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    climate = conn.execute(
        "SELECT * FROM climate WHERE TYPE =?", (id,)).fetchall()

    app.logger.info(json.dumps([tuple(row) for row in climate]))
    return json.dumps([tuple(row) for row in climate])


def publisherfunction(json_data):
    # app.logger.info(period, phen, advertise, country)
    phen = json_data['PHEN']
    advertise = json_data['ADVERTISE']
    period = json_data['PERIOD']
    country = json_data['COUNTRY']

    if phen == 'Temperature':
        phenomenon = 'tas'
        logger.info("temperature")
    else:
        phenomenon = 'pr'
        logger.info("pr")

    urlnew = ''
    #advertise function
    if advertise == 'Advertise':
        logger.info("advertise")
        urlnew = urlnew + 'UPCOMING phenomenon: ' + phen + ' in the period: ' + period
        conn = get_db_connection()
        sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = ?) OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
        conn.execute(sql, (urlnew, country, phen))
        conn.commit()


        conn.close()
    #publish function
    elif advertise == 'Publish':
        logger.info("publish")
        start = period.split('-')[0]
        end = period.split('-')[1]
        urlnew = urlnew + 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/' + \
            phenomenon + '/' + start + '/' + end + '/' + 'USA'
        conn = get_db_connection()
        sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = ?) OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
        logger.info(conn.execute(sql, (urlnew, country, phen)))
        logger.info(conn.commit())
        conn.close()


def subscriberfunction(json_data):
    phen = json_data['PHEN']
    id = json_data['ID']
    country = json_data['COUNTRY']
    subscribe = json_data['SUBSCRIBE']
    if not country:
        flash('Country code is required!')
    #subscribe function
    # subscribe_id = 0, Subscribe
    elif subscribe == 'Subscribe':
        default_msg = "Nothing available at this time"
        conn = get_db_connection()
        conn.execute("INSERT INTO climate (TYPE, ISO3,PHEN,SUBSCRIBE,default_msg) VALUES (?,?, ?, ?, ?)",
                     (id, country, phen, subscribe, default_msg)
                     )
        conn.commit()
        conn.close()
    #unsubscribe function
     # subscribe_id = 1, Unsubscribe
    elif subscribe == 'Unsubscribe':
        #print(id)
        conn = get_db_connection()
        sql = "DELETE FROM climate WHERE (ISO3 = ?) AND (TYPE = ?) AND (PHEN = ?)"
        conn.execute(sql, (country, id, phen))
        conn.commit()
        conn.close()


def to_next_broker(data):
    #send message to broker2
    url = "http://broker2:5000/sub"
    # data = {'ID': ID, 'PHEN': PHEN,
    #         'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
    app.logger.info(data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

# def from_last_broker(data):
    # display_sub(data)


if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug = True)
