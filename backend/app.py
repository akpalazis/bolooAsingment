from flask import Flask, request
from flask import jsonify
from flask import redirect
from flask_cors import CORS

from db import ShortURL
from db import db
from longurl.tools import convert_url
from longurl.tools import long_url_exist
from longurl.tools import fetch_long_entry
from longurl.tools import store_user_data

from shorturl.tools import fetch_short_url
from shorturl.tools import short_url_exist
from shorturl.tools import generate_short_url

app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
db.init_app(app)


@app.route('/', methods=['POST'])
def short_url():
    if request.method == 'POST':
        # Handle the POST request data
        url = request.json.get("url")
        if short_url_exist(url):
            return fetch_short_url(url)
        return generate_short_url(url)


@app.route('/<user_input>', methods=['GET'])
def long_url(user_input):
    if long_url_exist(user_input):
        url_entry = fetch_long_entry(user_input)
        url = convert_url(url_entry.long_url)
        client_ip = request.remote_addr
        store_user_data(url_entry, client_ip)
        return redirect(url)
    else:
        return jsonify({"msg": "Error no such a short url"})


@app.route("/fetch", methods=["GET"])
def fetch_all():
    # Query all data from the table
    all_data = ShortURL.query.all()
    dict_data = {}
    for i, data in enumerate(all_data):
        dict_data.update({i: {"long_url": data.long_url, "hits": data.hits, "uniq_hits": data.uniq_hits}})
    return jsonify({'entries': dict_data})


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
