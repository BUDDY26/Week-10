from flask import Flask, render_template, request
# import  sqlalchemy
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Setup app to use a sqlalchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampledb.db'
db = SQLAlchemy(app)


# Setup a simple tble for database


# Make a homepage
@app.route('/')
def homepage():
    return render_template('base.html' , name = " Ruben James Aleman ")

@app.route('/user/<name>')
def hello(name):
    listOfNames = [name, "Yoyo", "Yennifer"]
    return render_template('name.html', Sname=name, nameList=listOfNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name = None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

# Add in a page to view visitors



# Add the option to run this file directly
if __name__== "__main__":
    app.run(debug=True)