from flask import Flask, render_template, redirect, request
from db import SafeHood_db, reports
app = Flask(__name__)

@app.route('/')
def start():
    return (render_template("index.html"))

@app.route('/home')
def home():
    return redirect('/')

@app.route('/report')
def report():
    return (render_template("report.html"))

@app.route('/update_report',methods=["POST"])
def update_report():
    if request.method == "POST":
        name=request.form["user_name"]
        email=request.form["user_email"]
        phone=request.form["phone"]
        issuetype=request.form["user_issuetype"]
        location=request.form["user_location"]
        description=request.form["user_Description"]
        file = request.files["photo"]
        if file and file.filename != "":
            photo = file.read()  # Binary image
        else:
            photo = None
    reports(name, email, phone, issuetype, location, description, photo) 
    return (render_template("index.html"))

@app.route('/issues')
def issues():
    safehood_db=SafeHood_db()
    return (render_template("issue.html",Safehood_db=safehood_db))

@app.route('/about')
def about():
    return (render_template("about.html"))

@app.route('/help')
def help():
    return (render_template("help.html"))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None
    if request.method == 'POST':
        # Always fail the login
        error = "Wrong admin name or password"
    return render_template("admin.html", error=error)


if __name__=="__main__":
    app.run(debug=True)