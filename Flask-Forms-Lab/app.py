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

facebook_friends.append("Rani")
facebook_friends.append("Noura")
facebook_friends.append("Nebal")
facebook_friends.append("Lour")
facebook_friends.append("Lotfeh")
facebook_friends.append("Rawi")
facebook_friends.append("Seran")
facebook_friends.append("Laith")




facebook_friends.remove("Mark" and "Celina")


@app.route('/' ,  methods=['GET', 'POST'])# '/' for the default page
def login():
	if request.method == 'POST':
		username2 = request.form['username']
		password2 = request.form['password']
		if username2 == username and password2 == password :
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')


@app.route('/home')
def home():
	return render_template('home.html',facebook_friends = facebook_friends)

@app.route('/friend_exists/<string:name>',  methods=['GET', 'POST'])
def friend_exists(name):
	return render_template('friend_exists.html',facebook_friends = facebook_friends , name = name )

         
  
         
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)