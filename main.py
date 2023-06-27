from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    conn = sqlite3.connect('vedas.db')
    cursor = conn.cursor()

    # Execute the query to fetch date occurrences
    cursor.execute("SELECT substr(TIMESTAMP, 1, 11), COUNT(*) FROM threat GROUP BY substr(TIMESTAMP, 1, 11)")

    # Fetch all the date occurrences
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return {'data': data}

@app.route('/hourly_data')
def get_hourly_data():
    date = request.args.get('date')

    conn = sqlite3.connect('vedas.db')
    cursor = conn.cursor()

    cursor.execute("SELECT substr(TIMESTAMP, 13, 2), COUNT(*) FROM threat WHERE substr(TIMESTAMP, 1, 11) = ? GROUP BY substr(TIMESTAMP, 13, 2)", (date,))
    # Fetch all the hourly occurrences
    data = cursor.fetchall()
    print(data)

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return {'data': data}

if __name__ == '__main__':
    app.run(debug=True)
