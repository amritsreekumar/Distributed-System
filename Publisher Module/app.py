from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3

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
    conn = sqlite3.connect('/Users/amritsreekumar/Desktop/Distributed-System/Broker/database.db') #link to the broker is here
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/publisher1', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        #ISO3 = request.form['ISO3']
        PERIOD = request.form['PERIOD']
        #TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        ADVERTISE = request.form['ADV']
        #content = request.form['content']

        if PHEN == 'Temperature':
            phenomenon = 'tas'
        else:
            phenomenon = 'pr'
        urlnew = ''
        if ADVERTISE == 'Advertise':
            urlnew = urlnew + 'UPCOMING phenomenon: ' + PHEN + ' in the period: ' + PERIOD
            conn = get_db_connection()
            sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'USA') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
            conn.execute(sql, (urlnew, PHEN))
            conn.commit()
            conn.close()
        elif ADVERTISE == 'Publish':
            start = PERIOD.split('-')[0]
            end = PERIOD.split('-')[1]
            urlnew = urlnew + 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/' + phenomenon + '/' + start + '/' + end + '/' + 'USA'
            conn = get_db_connection()
            sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'USA') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
            conn.execute(sql, (urlnew, PHEN))
            conn.commit()
            conn.close()
    return render_template('publisher1.html')

@app.route('/publisher2', methods=('GET', 'POST'))
def index2():
    if request.method == 'POST':
        #ISO3 = request.form['ISO3']
        PERIOD = request.form['PERIOD']
        #TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        ADVERTISE = request.form['ADV']
        #content = request.form['content']

        if PHEN == 'Temperature':
            phenomenon = 'tas'
        else:
            phenomenon = 'pr'
        urlnew = ''
        if ADVERTISE == 'Advertise':
            urlnew = urlnew + 'UPCOMING phenomenon: ' + PHEN + ' in the period: ' + PERIOD
            conn = get_db_connection()
            sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'CAN') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
            conn.execute(sql, (urlnew, PHEN))
            conn.commit()
            conn.close()
        elif ADVERTISE == 'Publish':
            start = PERIOD.split('-')[0]
            end = PERIOD.split('-')[1]
            urlnew = urlnew + 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/' + phenomenon + '/' + start + '/' + end + '/' + 'USA'
            conn = get_db_connection()
            sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'CAN') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
            conn.execute(sql, (urlnew, PHEN))
            conn.commit()
            conn.close()
    return render_template('publisher2.html')


@app.route('/publisher3', methods=('GET', 'POST'))
def index3():
    if request.method == 'POST':
        #ISO3 = request.form['ISO3']
        PERIOD = request.form['PERIOD']
        #TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        ADVERTISE = request.form['ADV']
        #content = request.form['content']

        if PHEN == 'Temperature':
            phenomenon = 'tas'
        else:
            phenomenon = 'pr'
        urlnew = ''
        if ADVERTISE == 'Advertise':
            urlnew = urlnew + 'UPCOMING phenomenon: ' + PHEN + ' in the period: ' + PERIOD
            conn = get_db_connection()
            sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'MEX') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
            conn.execute(sql, (urlnew, PHEN))
            conn.commit()
            conn.close()
        elif ADVERTISE == 'Publish':
            start = PERIOD.split('-')[0]
            end = PERIOD.split('-')[1]
            urlnew = urlnew + 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/' + phenomenon + '/' + start + '/' + end + '/' + 'USA'
            conn = get_db_connection()
            sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'MEX') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
            conn.execute(sql, (urlnew, PHEN))
            conn.commit()
            conn.close()
    return render_template('publisher3.html')

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 
