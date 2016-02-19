#imports
from flask import Flask, url_for, request
from flask import render_template

#crear la aplicacion
app = Flask(__name__)

#funciones y clases de la aplicacion web
@app.route("/")
def hello():
	if request.method == 'POST':
		return "Esto es POST!"
	else:
		return "Hellow World!"

@app.route("/url")
def urlnueva():
	return "Yo soy otra URL"

@app.route("/post/<int:post_id>")
def mostrar_post(post_id):
	return "Post %d" % post_id

@app.route("/user/<username>")
def show_user_profile(username):
	return "User %s" % username

#funcion hello world con template
@app.route("/hello/")
@app.route("/hello/<name>")
def hello2(name=None):
	return render_template("hello.html", name = name)

#correr la aplicacion
if __name__ == "__main__":
	#indicar donde estan los archivos estaticos
	#url_for('satic', filename='style.css')
	app.debug = True
	app.run()