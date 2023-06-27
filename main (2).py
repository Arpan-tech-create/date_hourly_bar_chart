from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Data for the pie chart
    data = [
        ['Chrome', 60],
        ['Firefox', 30],
        ['Safari', 10]
    ]

    # Calculate the total sum for percentage calculation
    total = sum(value for _, value in data)

    # Calculate the percentage value for each slice
    chart_data = [[name, (value / total) * 100] for name, value in data]

    # Convert the data to JSON format
    chart_data_json = json.dumps(chart_data)

    return render_template('chart.html', chart_data=chart_data_json)

if __name__ == '__main__':
    app.run(debug=True)
