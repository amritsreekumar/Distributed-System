from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'

@app.route('/display', methods=('GET', 'POST'))
def display():
    conn = get_db_connection()
    climate = conn.execute('SELECT * FROM climate').fetchall()
    conn.close()
    return render_template('messagereceiver.html', climate=climate)

def get_db_connection():
    # print(os.getcwd())
    conn = sqlite3.connect('database.db')  # link to the broker is here
    conn.row_factory = sqlite3.Row
    return conn

def publisherfunction(period, phen, advertise):
    if phen == 'Temperature':
        phenomenon = 'tas'
    else:
        phenomenon = 'pr'
    urlnew = ''
    #advertise function
    if advertise == 'Advertise':
        urlnew = urlnew + 'UPCOMING phenomenon: ' + phen + ' in the period: ' + period
        conn = get_db_connection()
        sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'CAN') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
        conn.execute(sql, (urlnew, phen))
        conn.commit()
        conn.close()
    #publish function
    elif advertise == 'Publish':
        start = period.split('-')[0]
        end = period.split('-')[1]
        urlnew = urlnew + 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/' + phenomenon + '/' + start + '/' + end + '/' + 'USA'
        conn = get_db_connection()
        sql = "UPDATE climate SET default_msg = ? WHERE ((ISO3 = 'CAN') OR (ISO3 = 'ALL')) AND ((PHEN = ?) OR (PHEN = 'Both'))"
        conn.execute(sql, (urlnew, phen))
        conn.commit()
        conn.close()

def subscriberfunction(country, id, phen, subscribe):
    if not country:
            flash('Country code is required!')
    #subscribe function
    elif subscribe == 'Subscribe':
        default_msg = "Nothing available at this time"
        conn = get_db_connection()
        conn.execute("INSERT INTO climate (TYPE, ISO3,PHEN,SUBSCRIBE,default_msg) VALUES (?,?, ?, ?, ?)",
        (id,country,phen,subscribe,default_msg)
        )
        conn.commit()
        conn.close()
    #unsubscribe function
    elif subscribe == 'Unsubscribe':
        #print(id)
        conn = get_db_connection()
        sql = "DELETE FROM climate WHERE (ISO3 = ?) AND (TYPE = ?) AND (PHEN = ?)"
        conn.execute( sql , (country, id, phen))
        conn.commit()
        conn.close()



if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5003, debug = True)