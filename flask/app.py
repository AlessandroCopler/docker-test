from flask import Flask
from gevent.pywsgi import WSGIServer

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5001")
    # Production
    http_server = WSGIServer(('', 5001), app)
    http_server.serve_forever()