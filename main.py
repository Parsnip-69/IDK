from flask import Flask, render_template, request, redirect, url_for, session, Response
import send_email as email

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Hardcoded credentials (for demonstration)
USERNAME = "Scouts"
PASSWORD = "4thEG"

def check_auth(username, password):
    """Check if the entered username and password match the correct credentials."""
    return username == USERNAME and password == PASSWORD

def authenticate():
    """Send a 401 response that triggers the browser's login prompt."""
    return Response(
        "Authentication required", 401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )

@app.before_request
def check_login():
    """Run before every request to enforce authentication."""
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()  # Prompt login if authentication fails

@app.route('/')
def index():
    return render_template('index.html')

#About Us
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/trustee')
def trustee():
    return render_template('trustee.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/badges')
def badges():
    return render_template('badges.html')

@app.route('/sections')
def sections():
    return render_template('sections.html')

@app.route('/squirrels')
def squirrels():
    return render_template('squirrels.html')

#Sections
@app.route('/beavers')
def beavers():
    return render_template('beavers.html')

@app.route('/cubs')
def cubs():
    return render_template('cubs.html')

@app.route('/scouts')   
def scouts():
    return render_template('scouts.html')

@app.route('/join')
def join():
    return render_template('join.html')

#Other Pages
@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/additional')
def additional():
    return render_template('additional.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Sending Email
@app.route('/send')
def send():
    email.send_email()
    return redirect('http://www.onlinescoutmanager.co.uk/waiting-list/4th-east-grinstead-waiting-list/6789a6e2-d7e4-4342-ad3f-70bd71993ccd/apply')

if __name__ == '__main__':
    app.run()
