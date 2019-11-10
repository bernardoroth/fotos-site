from flask import Flask, request, redirect, make_response, render_template, url_for, jsonify, abort, flash
import api

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

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

@app.route('/new', methods=['GET'])
def new_picture():
    return render_template('new_picture.html')

@app.route('/api/new_picture', methods=['POST'])
def api_new_picture():
    print(request.form)
    print(request.files)
    return "", 204

if __name__ == "__main__":
    app.run(
        host='localhost',
        debug=True,
        port=8000
    )
