from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/beavers')
def beavers():
    return render_template('beavers.html')

@app.route('/cubs')
def cubs():
    return render_template('cubs.html')

@app.route('/scouts')   
def scouts():
    return render_template('scouts.html')

if __name__ == '__main__':
    app.run(debug=True)
