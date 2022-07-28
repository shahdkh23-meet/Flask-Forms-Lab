from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "shahdkh"
password = "123shahdkh"
facebook_friends=["Shahd","Yaso","Mark", "Maher", "Fouad", "Celina"]


@app.route('/')  # '/' for the default page
def login():
  return render_template('login.html')
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)