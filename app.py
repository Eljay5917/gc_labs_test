from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/whereami')
def whereami():
    return "cape coast"

@app.route('/foo/<name>')
def foo(name):
    return render_template("foo.html",to=name)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')