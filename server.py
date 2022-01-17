from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "its a secret"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
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

if __name__ == "__main__":
    app.run(debug=True)

