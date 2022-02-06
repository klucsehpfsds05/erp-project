from flask import Flask,render_template


app = Flask(__name__)

students =[
{"regdno":2000030695,
 "name":"prasanth",
 "course":"PFSD"},

 {"regdno":2000030000,
 "name":"sai",
 "course":"AI for DS"},

 {"regdno":2000030001,
 "name":"uday",
 "course":"OSD"}
]



@app.route('/')
def home():
    return render_template("home.html",title="Home",students=students)

@app.route('/login')
def login():
   return render_template("login.html",title="Login")

@app.route('/register')
def register():
    return render_template("register.html",title="Register")

@app.route('/logout')
def logout():
    return "logged out"

@app.route('/profile')
def profile():
    return "My Profile"

@app.route('/attendance')
def attendance():
    return "100%"

@app.route('/marks')
def marks():
    return "My Marks"

@app.route('/about')
def about():
    return "contact us"








if __name__ == "__main__":
    app.run(debug= True)