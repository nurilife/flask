#!/usr/bin/env pyton
# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", name="jeon")
if __name__ == "__main__":
    app.run(host='192.168.0.11', port=8888, debug=True)