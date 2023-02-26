from flask import Flask, render_template
import os
import utils
from flask import jsonify

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config["JSON_AS_ASCII"] = False
@app.route("/")
def root():
    return render_template('main.html')

@app.route("/time")
def get_time():
    return utils.get_time()

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify(data)

@app.route("/ajax", methods = ["get","post"])
def root2():
    return "10000"

if __name__ == '__main__':
    app.run()
