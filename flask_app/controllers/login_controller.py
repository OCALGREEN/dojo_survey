from flask  import render_template, redirect, request, session
from flask_app import app
from flask_app.models.login import LogIn

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if not LogIn.validator(request.form):
        return redirect("/")

    return redirect('/results')

@app.route('/results')
def results():
    return render_template(
        'results.html',
        user_name = session['name'],
        dojo_location = session['location'],
        favorite_language = session['language'],
        user_comment = session['comment'],
    )
