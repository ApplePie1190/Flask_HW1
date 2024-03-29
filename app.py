from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/clothes')
def clothes():
    return render_template('clothes.html')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket')
def jacket():
    return render_template('jacket.html')

