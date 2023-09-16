from flask import Flask, render_template, request, redirect, flash
from models import student_model
import os


app = Flask(__name__)
app.secret_key = "your_secret_key"

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/student_database")
app.config["MONGO_URI"] = MONGO_URI


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("createpage.html")

    if request.method == "POST":
        data = request.form.to_dict()
        student_model.create_student(data)
        flash("Student created successfully", "success")
        return redirect("/")


@app.route("/")
def retrieve_list():
    students = student_model.get_all_students()
    return render_template("datalist.html", students=students)


@app.route("/<string:id>")
def retrieve_student(id):
    student = student_model.get_student_by_id(id)
    if student:
        return render_template("data.html", student=student)
    return f"Student with id={id} doesn't exist"


@app.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        student = student_model.get_student_by_id(id)
        if student:
            return render_template("update.html", student=student)
        else:
            return f"Student with id={id} doesn't exist"

    if request.method == "POST":
        data = request.form.to_dict()
        student_model.update_student(id, data)
        flash("Student updated successfully", "success")
        return redirect("/")


@app.route("/delete/<string:id>", methods=["POST"])
def delete(id):
    student_model.delete_student(id)
    flash("Student deleted successfully", "success")
    return redirect("/")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"))
