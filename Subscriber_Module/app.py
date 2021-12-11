from time import sleep
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3
import os
import requests
import json
# from Broker.pubsub import subscriberfunction

#test
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'


# def get_db_connection():
#     # link to the broker is here
#     # print(os.getcwd())
#     conn = sqlite3.connect('./data/database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


@app.route('/subscriber1', methods=('GET', 'POST'))
def subscriber1():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(url, data=json.dumps(data), headers=headers)
    return render_template('subscriber1.html')


@app.route('/subscriber2', methods=('GET', 'POST'))
def subscriber2():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber2.html')


@app.route('/subscriber3', methods=('GET', 'POST'))
def subscriber3():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber3.html')


@app.route('/subscriber4', methods=('GET', 'POST'))
def subscriber4():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber4.html')


@app.route('/subscriber5', methods=('GET', 'POST'))
def subscriber5():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber5.html')


@app.route('/subscriber6', methods=('GET', 'POST'))
def subscriber6():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber6.html')


@app.route('/subscriber7', methods=('GET', 'POST'))
def subscriber7():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber7.html')


@app.route('/subscriber8', methods=('GET', 'POST'))
def subscriber8():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber8.html')


@app.route('/subscriber9', methods=('GET', 'POST'))
def subscriber9():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber9.html')


@app.route('/subscriber10', methods=('GET', 'POST'))
def subscriber10():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber10.html')


@app.route('/subscriber11', methods=('GET', 'POST'))
def subscriber11():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber11.html')


@app.route('/subscriber12', methods=('GET', 'POST'))
def subscriber12():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHEN = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        PUB_SUB_ID = "SUB"

        url = "http://consumer:5000/sub"
        data = {'ID': ID, 'PHEN': PHEN,
                'SUBSCRIBE': SUBSCRIBE, 'COUNTRY': COUNTRY, "PUB_SUB_ID": PUB_SUB_ID}
        app.logger.info(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('subscriber12.html')


@app.route('/displaysubscriber1', methods=('GET', 'POST'))
def displaysubscriber1():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/subscriber_view"
    data = {'ID': "subscriber1"}
    app.logger.info("inside displaysubscriber1")
    app.logger.info(type(data))
    headers = {'Content-type': 'application/json',
               'Accept': None}
    requests.post(url, data=json.dumps(data), headers=headers)
    #app.logger.info("NIKHILLLLL")

    # return render_template('displaysubscriber1.html', climate=climate)
    # return render_template('displaysubscriber1.html', jsonfile=climate.json())
    return render_template('displaysubscriber1.html')


@app.route('/displaysubscriber2')
def displaysubscriber2():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber2"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info("NIKHILLLLL")
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber2.html', jsonfile=climate.json())


@app.route('/displaysubscriber3')
def displaysubscriber3():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber3"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber3.html', jsonfile=climate.json())


@app.route('/displaysubscriber4')
def displaysubscriber4():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber4"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber4.html', jsonfile=climate.json())


@app.route('/displaysubscriber5')
def displaysubscriber5():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber5"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber5.html', jsonfile=climate.json())


@app.route('/displaysubscriber6')
def displaysubscriber6():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber6"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber6.html', jsonfile=climate.json())


@app.route('/displaysubscriber7')
def displaysubscriber7():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber7"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber7.html', jsonfile=climate.json())


@app.route('/displaysubscriber8')
def displaysubscriber8():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber8"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber8.html', jsonfile=climate.json())


@app.route('/displaysubscriber9')
def displaysubscriber9():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber9"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber9.html', jsonfile=climate.json())


@app.route('/displaysubscriber10')
def displaysubscriber10():
    # conn = get_db_connection()
    # climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    # conn.close()
    url = "http://consumer:5000/susbscriber_view"
    data = {'ID': "subscriber10"}
    app.logger.info(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    climate = requests.post(url, data=json.dumps(data), headers=headers)
    app.logger.info(type(climate))
    app.logger.info(climate.json())
    # return render_template('displaysubscriber1.html', climate=climate)
    return render_template('displaysubscriber10.html', jsonfile=climate.json())





if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug = True)
