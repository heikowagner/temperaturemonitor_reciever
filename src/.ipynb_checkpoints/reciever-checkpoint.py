#from flask import Flask
#import flask
#import json
#app = Flask(__name__)
#PORT = 65432        # The port used by the server

#@app.route('/')
#def hello_world():
#    return flask.Response(json.dumps({"status": "SUCCESS", "msg": "Berechnung schon fertig:))))"}), status=200, content_type="application/json")

#if __name__ == '__main__':
#    app.run(debug=True,host='0.0.0.0', port=PORT)

from sanic import Sanic
from sanic.response import json
import time
import asyncio

app = Sanic(name='Reciever')

PORT = 65432        # The port used by the server

@app.route('/')
async def hello_world(request):
    await asyncio.sleep(50) #Die Berechnung
    return json({"status": "SUCCESS", "msg": "Berechnung schon fertig:))))"}, status=200)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=PORT)