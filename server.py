from flask import Flask, render_template, request, redirect
import database
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/course", methods=['GET','POST'])
def course():
    if request.method == "GET":
        return render_template("course.html")
    else:
        name = request.form['name']
        fees = request.form['fees']
        status = database.addCourse(name, fees)
        return status

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    if request.method == "GET":
        return render_template("feedback.html")
    else:
        user_feedback = request.form['feedback']
        print(user_feedback)
        return redirect("/feedback")
app.run(debug=True)