from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/trustee')
def trustee():
    return render_template('trustee.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/squirrels')
def squirrels():
    return render_template('squirrels.html')

@app.route('/beavers')
def beavers():
    return render_template('beavers.html')

@app.route('/cubs')
def cubs():
    return render_template('cubs.html')

@app.route('/scouts')   
def scouts():
    return render_template('scouts.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

if __name__ == '__main__':
    app.run(debug=True)
