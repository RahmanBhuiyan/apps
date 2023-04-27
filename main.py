from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import urllib.parse

password = 'Error@4044'
encoded_password = urllib.parse.quote_plus(password)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:'+ encoded_password + '@localhost/bug_rangers'

# Create a SQLAlchemy object and bind it to the app
db = SQLAlchemy(app)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Error@4044'
# app.config['MYSQL_DB'] = 'database_name'

# db = MySQL(app)

class contacts(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    # variable pass in teamplate 
    # name ="chill"
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact",methods=["GEt","POST"])
def contact():
    if (request.method=='POST'):
        #add entry to the database
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        #connect database table
        entry=contacts(name=name,email=email,phone_number = phone,message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(port=0,debug=True)