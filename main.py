from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'bazarvito_secret_key'


@app.route('/')
def index():
    return render_template('index.html', title='Bazarvito')


if __name__ == '__main__':
    # create_db()
    app.run(host='127.0.0.1', port=8080)