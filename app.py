import os
import signal
from flask import Flask
from calculator import sum

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def calculate_sum():
    numbers = (12, 10)
    page = '<html><body><h1>'
    page += 'Sum of two number {} + {} = '.format(*numbers)
    page += str(sum.sum(*numbers))
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
