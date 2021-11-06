from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3
import os
from Broker.pubsub import subscriberfunction

#test
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'


@app.route('/displaysubscriber1')
def displaysubscriber1():
    conn = get_db_connection()
    climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber1"').fetchall()
    conn.close()
    return render_template('displaysubscriber1.html', climate=climate)


@app.route('/displaysubscriber2')
def displaysubscriber2():
    conn = get_db_connection()
    climate = conn.execute('SELECT * FROM climate WHERE TYPE = "subscriber2"').fetchall()
    conn.close()
    return render_template('displaysubscriber2.html', climate=climate)

def get_db_connection():
    # link to the broker is here
    # print(os.getcwd())
    conn = sqlite3.connect('./data/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/subscriber1', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHENOMENON = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        #content = request.form['content']

        subscriberfunction(COUNTRY, ID, PHENOMENON, SUBSCRIBE)
        #write subscription logic here, add to db when we subscribe, remove from db when we unsubscribe
        # if not COUNTRY:
        #     flash('Country code is required!')
        # #subscribe function
        # elif SUBSCRIBE == 'Subscribe':
        #     default_msg = "Nothing available at this time"
        #     conn = get_db_connection()
        #     conn.execute("INSERT INTO climate (TYPE, ISO3,PHEN,SUBSCRIBE,default_msg) VALUES (?,?, ?, ?, ?)",
        #     (ID,COUNTRY,PHENOMENON,SUBSCRIBE,default_msg)
        #     )
        #     conn.commit()
        #     conn.close()
        # #unsubscribe function
        # elif SUBSCRIBE == 'Unsubscribe':
        #     print(ID)
        #     conn = get_db_connection()
        #     sql = "DELETE FROM climate WHERE (ISO3 = ?) AND (TYPE = ?) AND (PHEN = ?)"
        #     conn.execute( sql , (COUNTRY, ID, PHENOMENON))
        #     conn.commit()
        #     conn.close()
    return render_template('subscriber1.html')

@app.route('/subscriber2', methods=('GET', 'POST'))
def index2():
    if request.method == 'POST':
        COUNTRY = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        ID = request.form['TYPE']
        PHENOMENON = request.form['PHEN']
        SUBSCRIBE = request.form['SUBSCRIBE']
        #content = request.form['content']


        #write subscription logic here, add to db when we subscribe, remove from db when we unsubscribe
        if not COUNTRY:
            flash('Country code is required!')
        #subscribe function
        elif SUBSCRIBE == 'Subscribe':
            default_msg = "Nothing available at this time"
            conn = get_db_connection()
            conn.execute("INSERT INTO climate (TYPE, ISO3,PHEN,SUBSCRIBE,default_msg) VALUES (?,?, ?, ?, ?)",
            (ID,COUNTRY,PHENOMENON,SUBSCRIBE,default_msg)
            )
            conn.commit()
            conn.close()
        #unsubscribe function
        elif SUBSCRIBE == 'Unsubscribe':
            conn = get_db_connection()
            sql = "DELETE FROM climate WHERE (ISO3 = ?) AND (TYPE = ?) AND (PHEN = ?)"
            conn.execute( sql , (COUNTRY, ID, PHENOMENON))
            conn.commit()
            conn.close()
    return render_template('subscriber2.html')

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5002, debug = True)
