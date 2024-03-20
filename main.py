from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'bazarvito_secret_key'


@app.route('/index')
def index():
    return render_template('index.html', title='Bazarvito')