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
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/subscriber1', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        ISO3 = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        #content = request.form['content']

        if not ISO3:
            flash('Country code is required!')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO climate (ISO3,PERIOD,TYPE,PHEN) VALUES (?, ?, ?)",
            (ISO3,TYPE,PHEN)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('subscriber1'))

    return render_template('subscriber1.html')

@app.route('/subscriber2', methods=('GET', 'POST'))
def index2():
    if request.method == 'POST':
        ISO3 = request.form['ISO3']
        #PERIOD = request.form['PERIOD']
        TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        #content = request.form['content']

        if not ISO3:
            flash('Country code is required!')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO climate (ISO3,PERIOD,TYPE,PHEN) VALUES (?, ?, ?)",
            (ISO3,TYPE,PHEN)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('subscriber2'))

    return render_template('subscriber2.html')

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 
