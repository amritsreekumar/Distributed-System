import json
from flask import Flask, render_template, request, url_for, flash, redirect
import flask
from werkzeug.exceptions import abort
import sqlite3
import os
import logging
import jsonify


topics = ["CAN/tas", "USA/tas", "MEX/tas", "IND/tas"]
subscribers = ["subscriber1", "subscriber2", "subscriber3", "subscriber4"]

app = Flask(__name__)

logger = logging.getLogger('werkzeug')  # grabs underlying WSGI logger
handler = logging.FileHandler('test.log')  # creates handler for the log file
logger.addHandler(handler)  # adds handler to the werkzeug WSGI logger
app.config['SECRET_KEY'] = 'abcd'


# @app.route('/displaypublisher', methods=('GET', 'POST'))
# def displaypublisher():
#     conn = get_db_connection(period, phen, advertise,
#                              country)  # take this from post
#     climate = conn.execute('SELECT * FROM climate').fetchall()
#     conn.close()
#     return render_template('messagereceiver.html', climate=climate)


def get_db_connection():
    # print(os.getcwd())
    conn = sqlite3.connect('./data/database.db')  # link to the broker is here
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/display', methods=('GET', 'POST'))
def display():
    conn = get_db_connection()
    json_data = flask.request.json
    app.logger.info(json_data)
    #ISO3 = request.form['ISO3']
    # PERIOD = json_data['PERIOD']
    # #TYPE = request.form['TYPE']
    # PHEN = json_data['PHEN']
    # ADVERTISE = json_data['ADVERTISE']
    # COUNTRY = json_data['COUNTRY']
    # app.logger.info(PERIOD, PHEN, ADVERTISE, COUNTRY)
    # PUB_SUB_ID = json_data("PUB_SUB_ID")
    # if PUB_SUB_ID == "PUB":
    #     publisherfunction(json_data)
    # elif PUB_SUB_ID == "SUB":
    #     subscriberfunction(json_data)
    publisherfunction(json_data)
    climate = conn.execute('SELECT * FROM climate').fetchall()
    # print(json_data)
    conn.close()
    # return json_data


@app.route('/display_sub', methods=('GET', 'POST'))
def display_sub():
    conn = get_db_connection()
    json_data = flask.request.json
    app.logger.info(json_data)
    subscriberfunction(json_data)
    climate = conn.execute('SELECT * FROM climate').fetchall()
    # print(json_data)
    conn.close()
    

@app.route('/print', methods=('GET', 'POST'))
def print():
    conn = get_db_connection()
    climate = conn.execute('SELECT * FROM climate').fetchall()
    return render_template('messagereceiver.html', climate=climate)


@app.route('/sub1_print', methods=('GET', 'POST'))
def sub1_print():
    json_data = flask.request.json
    id = json_data["ID"]
    # ID = str(ID)
    app.logger.info(id)
    conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    climate = conn.execute(
        "SELECT * FROM climate WHERE TYPE =?", (id,)).fetchall()
    # sql = "SELECT * FROM climate WHERE TYPE = ?"
    # app.logger.info(conn.execute(sql, (ID)).fetchall())
    # app.logger.info(conn.commit())
    # # climate = "nikhil"
    app.logger.info(json.dumps([tuple(row) for row in climate]))
    # return render_template('displaysubscriber1.html', climate=climate)
    # return json.dumps(climate)
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

if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug = True)
