from TrainingTool import app, db, redirect, url_for


@app.route("/")
def home():
    return redirect(url_for("Subject.addsubject"))


if __name__ == "__main__":
    app.run(host="192.168.29.227",port=80)
