from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return render_template('index.html', username=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]        
        # userExists(username, password)
        return redirect(url_for('index', name=username))
    else:
        return render_template('login.html')

@app.route('/about')
def about():
    return 'The About Page'