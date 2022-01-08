from flask import Flask, render_template, request, redirect
app = Flask('app')


@app.route('/login')
def login():
  return render_template("login.html")
@app.route('/signup')
def signup():
  return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
  return render_template(
    "dashboard.html"
  )
@app.route("/")
def homescreen():
  username = request.cookies.get('u')
  password = request.cookies.get('p')
  if not username and not password:
    return redirect("/login")
  return redirect("/dashboard")


app.run(host='0.0.0.0', port=8080)
