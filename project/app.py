from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def reqeusts():
    return render_template("index.html")

#app.route('/', methods=['POST'])
#def process_form():
   # country = request.form['country']
    #weather = request.form['weather']

    # Process the data or perform any desired actions

    
    #return render_template('result_template.html', country=country, weather=weather)

@app.route('/results')
def results():
    return render_template("results.html")
@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"),404
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')