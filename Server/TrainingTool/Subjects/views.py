from TrainingTool import db
from flask import Blueprint, render_template, redirect, url_for
from TrainingTool.Models import Subject
from TrainingTool.Subjects.forms import AddSubject
import sys

subject_blueprint = Blueprint("Subject", __name__, template_folder="templates",static_folder="static")


@subject_blueprint.route("/add", methods=["GET", "POST"])
def addsubject():
    form = AddSubject()
    try:
        if form.validate_on_submit():
            name = form.Subject_name.data
            subject = Subject(name)
            subject.insert()
            return redirect(url_for("Topic.addtopic"))
    except Exception as e:
        print(e,file=sys.stderr)
    return render_template("addsubject.html", form=form)
