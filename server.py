from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    if request.method == "GET":
        return render_template("feedback.html")
    else:
        user_feedback = request.form['feedback']
        print(user_feedback)
        return redirect("/feedback")
app.run(debug=True)