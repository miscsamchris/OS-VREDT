from TrainingTool import app, db, redirect, url_for


@app.route("/")
def home():
    return redirect(url_for("Subject.addsubject"))


if __name__ == "__main__":
    app.run(host="HOSTNAME",port=80)
