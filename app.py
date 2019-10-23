from flask import Flask, request, redirect, make_response, render_template, url_for, jsonify, abort, flash
import os, time, datetime, re, mimetypes, traceback, base64

app = Flask(__name__)

UNPROC_ENTITY = 422
SERVER = 500
NOT_FOUND = 404
FORBIDDEN = 500

@app.route('/')
def root():
    return jsonify("root")

@app.route('/fotos')
def nopage(): return redirect(url_for('home', page=1))
@app.route('/fotos/page')
def home(page):
    pass

if __name__ == "__main__":
    app.run(
        host="localhost",
        port=8000,
        debug=True
    )
