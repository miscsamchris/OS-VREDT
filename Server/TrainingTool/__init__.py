import os
from flask import Flask, render_template, redirect, url_for
from flask_restful import Api
import MySQLdb

direc = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY
api = Api(app=app)
class Connection():
    def __init__(self):
        self.host="#PlanetScale HostName"
        self.user="#PlanetScale UserName"
        self.passwd="#PlanetScale Password"
        self.db_name="#PlanetScale DBName"
        self.ssl={"ca": "#Path to ca"}
    def connect(self):
        self.db=MySQLdb.connect(
        host=self.host,
        user=self.user,
        passwd=self.passwd,
        db=self.db_name,
        ssl=self.ssl,
        )
        return self.db
    def close(self):
        self.db.close()

db=Connection()
from TrainingTool.Topics.views import topic_blueprint
from TrainingTool.Subjects.views import subject_blueprint
from TrainingTool.Videos.views import video_blueprint
from TrainingTool.RestAPI.RESTfulAPI import (
    SubjectRest,
    Subjects,
    TopicRest,
    Topics,
    VideoRest,
    Videos,
    IntentRest,
    ChatBotIntentsRest,
)

app.register_blueprint(topic_blueprint, url_prefix="/topic")
app.register_blueprint(subject_blueprint, url_prefix="/subject")
app.register_blueprint(video_blueprint, url_prefix="/video")
api.add_resource(SubjectRest, "/rest/subject/<string:name>/")
api.add_resource(Subjects, "/rest/subject/")
api.add_resource(TopicRest, "/rest/topic/<string:name>/")
api.add_resource(Topics, "/rest/topic/")
api.add_resource(VideoRest, "/rest/video/<int:id>/")
api.add_resource(Videos, "/rest/video/name/<string:name>/")
api.add_resource(ChatBotIntentsRest, "/rest/chatbot/<int:id>/")
api.add_resource(IntentRest, "/rest/intent/<string:name>/")
