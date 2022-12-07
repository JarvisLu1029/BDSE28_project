from flask import Flask , make_response
import json
import requests as req

app = Flask(__name__)

my_headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
}

@app.route('/taipei', methods=["GET"])

def taipei():
    url = ""
    res = req.get( ,headers = my_headers )
    reponse =make_response( json.dump(res.json(),ensure_ascii=False))
