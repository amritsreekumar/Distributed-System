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

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        ISO3 = request.form['ISO3']
        PERIOD = request.form['PERIOD']
        TYPE = request.form['TYPE']
        PHEN = request.form['PHEN']
        #content = request.form['content']

        if not ISO3:
            flash('Country code is required!')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO climate (ISO3,PERIOD,TYPE,PHEN) VALUES (?, ?, ?, ?)",
            (ISO3,PERIOD,TYPE,PHEN)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 
