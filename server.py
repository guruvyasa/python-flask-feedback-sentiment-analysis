from flask import Flask, render_template, request, redirect, url_for
import database
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/course", methods=['GET','POST'])
def course():
    if request.method == "GET":
        status = request.args.get("status",0)
        return render_template("course.html", status=status,courses= database.getCourses())
    else:
        name = request.form['name']
        fees = request.form['fees']
        status = database.addCourse(name, fees)
        return redirect("/course?status="+status)

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    if request.method == "GET":
        status = request.args.get("status",0)
        print(status)
        return render_template("feedback.html",status=status, courses=database.getCourses())
    else:
        user_feedback = request.form['feedback']
        course_id = request.form['course']
        status = database.addFeedback(user_feedback, course_id)
        return redirect("/feedback?status="+status)
app.run(debug=True)