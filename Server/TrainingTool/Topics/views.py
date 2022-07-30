import re
from TrainingTool import db
from flask import Blueprint, render_template, redirect, url_for, request
from TrainingTool.Models import Topic, Subject, ChatBot, Intent
from TrainingTool.Topics.forms import AddTopics, AddIntent
import json, requests
import sys
import traceback


topic_blueprint = Blueprint("Topic", __name__, template_folder="templates",static_folder="static")


def createcb(name, topic_id):
    chatbot_name = name.replace(" ","")
    url = "https://api.wit.ai/apps?v=20210606"
    payload = (
        '{"name": "'
        + chatbot_name
        + '", "lang": "en", "private": true,"timezone": "Europe/Brussels"}'
    )
    headers = {
        "Authorization": "Bearer # Admin Token From wit.ai",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    chatbot_uid = res["app_id"]
    chatbot_access_code = res["access_token"]
    cb = ChatBot(chatbot_name, "20210606", chatbot_access_code, chatbot_uid, topic_id)
    return cb


@topic_blueprint.route("/add", methods=["GET", "POST"])
def addtopic():
    form = AddTopics()
    try:
        subjects = Subject.select_all()
        choice = [(i.id, i.subject_name) for i in list(subjects)]
        form.Subject_name.choices = choice
        if form.is_submitted():
            name = form.Topic_name.data
            sub_id = form.Subject_name.data
            desc = form.Topic_Description.data
            topic = Topic(name, sub_id, desc)
            topic.insert()
            chatbot = createcb(topic.topic_name + "ChatBot", topic.id)
            chatbot.insert()
            return redirect(url_for("Topic.addintent", cbid=chatbot.id))
    except Exception as e:
        print(e,file=sys.stderr)
    return render_template("addtopic.html", form=form)


@topic_blueprint.route("/Addintent/<int:cbid>/", methods=["GET", "POST"])
def addintent(cbid):
    form = AddIntent()
    try:
        if form.is_submitted():
            intent_name = form.intent_name.data.replace(" ", "_")
            intent_response = form.intent_response.data
            chatbot = ChatBot.filter_by_id(cbid)
            access_code = chatbot.chatbot_access_code
            version = chatbot.chatbot_version
            url = "https://api.wit.ai/intents?v=" + version
            payload = '{"name": "' + intent_name + '"}'
            headers = {
                "Authorization": "Bearer " + access_code,
                "Content-Type": "application/json",
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            res = json.loads(response.text)
            intent_uid = res["id"]
            if request.method == "POST" and len(list(request.form.keys())) > 0:
                keys = list(request.form.keys())
                trainingdata = [request.form[x] for x in keys if "data_query" in x]
                if len(trainingdata) > 0:
                    url = "https://api.wit.ai/utterances?v=" + version
                    headers = {
                        "Authorization": "Bearer " + access_code,
                        "Content-Type": "application/json",
                    }
                    payload = [
                        {"text": x, "intent": intent_name, "entities": [], "traits": []}
                        for x in trainingdata
                    ]
                    pl = "["
                    for i in payload:
                        pl += str(i) + ","
                    pl += "]"
                    response = requests.request("POST", url, headers=headers, data=pl)
                    intent = Intent(intent_name, intent_uid, cbid, intent_response)
                    intent.insert()
                return redirect(url_for("Topic.addintent", cbid=cbid))
    except Exception as e:
        print(traceback.format_exc())
    return render_template("addintent.html", form=form)
