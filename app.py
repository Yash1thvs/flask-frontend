from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route("/test")
def test():
    return {"test": "hello"}


if __name__ == '__main__':
    app.run(debug=True)