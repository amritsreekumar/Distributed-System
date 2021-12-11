from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3
import os
# import Broker
# from Broker.pubsub import publisherfunction
import requests
import json
#test
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'


@app.route('/display')
def display():
    conn = get_db_connection()
    climate = conn.execute('SELECT * FROM climate').fetchall()
    conn.close()
    return render_template('display.html', climate=climate)

def get_db_connection():
    # print(os.getcwd())
    conn = sqlite3.connect('./data/database.db')  # link to the broker is here
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/publisher1', methods=('GET', 'POST'))
def publisher1():
    if request.method == 'POST':
        #ISO3 = request.form['ISO3']
        PERIOD = request.form['PERIOD']
        #TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        ADVERTISE = request.form['ADV']
        COUNTRY = 'USA'
        PUB_SUB_ID = "PUB"
        subscribe_id = "0"
        #content = request.form['content']
        url = "http://localhost:5003/pub"
        data = {'PERIOD': PERIOD, 'PHEN': PHEN,
                'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID, "subscribe_id": subscribe_id}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
  
    return render_template('publisher1.html')

@app.route('/publisher2', methods=('GET', 'POST'))
def publisher2():
    if request.method == 'POST':
        #ISO3 = request.form['ISO3']
        PERIOD = request.form['PERIOD']
        #TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        ADVERTISE = request.form['ADV']
        COUNTRY = 'CAN'
        #content = request.form['content']
        PUB_SUB_ID = "PUB"
        subscribe_id = "0"
        #content = request.form['content']
        url = "http://localhost:5003/pub"
        data = {'PERIOD': PERIOD, 'PHEN': PHEN,
                'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID, "subscribe_id": subscribe_id}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

        # if PHEN == 'Temperature':
        #     phenomenon = 'tas'
        # else:
        #     phenomenon = 'pr'
        # urlnew = ''
        # #advertise function
        # if ADVERTISE == 'Advertise':
        #     urlnew = urlnew + 'UPCOMING phenomenon: ' + PHEN + ' in the period: ' + PERIOD
        #     conn = get_db_connection()
        #     sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'CAN') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
        #     conn.execute(sql, (urlnew, PHEN))
        #     conn.commit()
        #     conn.close()
        # #publish function
        # elif ADVERTISE == 'Publish':
        #     start = PERIOD.split('-')[0]
        #     end = PERIOD.split('-')[1]
        #     urlnew = urlnew + 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/' + phenomenon + '/' + start + '/' + end + '/' + 'USA'
        #     conn = get_db_connection()
        #     sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'CAN') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
        #     conn.execute(sql, (urlnew, PHEN))
        #     conn.commit()
        #     conn.close()

    return render_template('publisher2.html')


@app.route('/publisher3', methods=('GET', 'POST'))
def publisher3():
    if request.method == 'POST':
        #ISO3 = request.form['ISO3']
        PERIOD = request.form['PERIOD']
        #TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        ADVERTISE = request.form['ADV']

        #content = request.form['content']
        COUNTRY = 'MEX'
        PUB_SUB_ID = "PUB"
        subscribe_id = "0"
        #content = request.form['content']
        url = "http://localhost:5003/pub"
        data = {'PERIOD': PERIOD, 'PHEN': PHEN,
                'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID, "subscribe_id": subscribe_id}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
    return render_template('publisher3.html')



# @app.route('/publisher4', methods=('GET', 'POST'))
# def publisher4():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'IND'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
 
#     return render_template('publisher4.html')


# @app.route('/publisher5', methods=('GET', 'POST'))
# def publisher5():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'AFG'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#         # print(r.status_code)
#         # publisherfunction(PERIOD, PHEN, ADVERTISE) #send the message here
#         # if PHEN == 'Temperature':
#         #     phenomenon = 'tas'
#         # else:
#         #     phenomenon = 'pr'
#         # urlnew = ''
#         # #advertise function
#         # if ADVERTISE == 'Advertise':
#         #     urlnew = urlnew + 'UPCOMING phenomenon: ' + PHEN + ' in the period: ' + PERIOD
#         #     conn = get_db_connection()
#         #     sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'USA') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
#         #     conn.execute(sql, (urlnew, PHEN))
#         #     conn.commit()
#         #     conn.close()
#         # #publish function
#         # elif ADVERTISE == 'Publish':
#         #     start = PERIOD.split('-')[0]
#         #     end = PERIOD.split('-')[1]
#         #     urlnew = urlnew + 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/' + phenomenon + '/' + start + '/' + end + '/' + 'USA'
#         #     conn = get_db_connection()
#         #     sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'USA') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
#         #     conn.execute(sql, (urlnew, PHEN))
#         #     conn.commit()
#         #     conn.close()
#     return render_template('publisher5.html')


# @app.route('/publisher6', methods=('GET', 'POST'))
# def publisher6():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'ALB'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('publisher6.html')


# @app.route('/publisher7', methods=('GET', 'POST'))
# def publisher7():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'BGR'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('publisher7.html')


# @app.route('/publisher8', methods=('GET', 'POST'))
# def publisher8():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'CMR'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('publisher8.html')


# @app.route('/publisher9', methods=('GET', 'POST'))
# def publisher9():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'IOT'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('publisher9.html')


# @app.route('/publisher10', methods=('GET', 'POST'))
# def publisher10():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'TCD'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('publisher10.html')


# @app.route('/publisher11', methods=('GET', 'POST'))
# def publisher11():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'COL'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('publisher11.html')


# @app.route('/publisher12', methods=('GET', 'POST'))
# def publisher12():
#     if request.method == 'POST':
#         #ISO3 = request.form['ISO3']
#         PERIOD = request.form['PERIOD']
#         #TYPE = request.form['TYPE']
#         PHEN = request.form['PHEN']
#         ADVERTISE = request.form['ADV']
#         COUNTRY = 'CYP'
#         #content = request.form['content']
#         url = "http://broker:5000/pub"
#         data = {'PERIOD': PERIOD, 'PHEN': PHEN,
#                 'ADVERTISE': ADVERTISE, 'COUNTRY': COUNTRY}
#         app.logger.info(data)
#         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#     return render_template('publisher12.html')


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=5001, debug = True)
