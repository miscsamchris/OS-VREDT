from flask_restful import Resource, Api
from flask import Blueprint
from TrainingTool import db, app

from TrainingTool.Models import Intent, Meeting, Subject, Topic, Video, ChatBot


class SubjectRest(Resource):
    def get(self, name):
        subject = Subject.filter_by_name(name)
        if subject != None:
            return {
                "code": 200,
                "id": subject.id,
                "Subject Name": subject.subject_name,
                "Topics": [
                    {"Topic ID": i.id, "Topic Name": i.topic_name}
                    for i in list(Topic.select_all())
                    if i.subject_id == subject.id
                ],
            }
        return {"code": 404, "Message": "No Data Found"}, 404


class Subjects(Resource):
    def get(self):
        subjects = Subject.select_all()
        if subjects != None:
            subs = []
            for subject in subjects:
                subs.append(
                    {
                        "id": subject.id,
                        "Subject Name": subject.subject_name,
                        "Topics": [
                            {"Topic ID": i.id, "Topic Name": i.topic_name}
                            for i in list(Topic.select_all())
                            if i.subject_id == subject.id
                        ],
                    }
                )
            return {"code": 200, "subjects": subs}
        return {"code": 404, "Message": "No Data Found"}, 404


class TopicRest(Resource):
    def get(self, name):
        topic = Topic.filter_by_name(name)
        if topic != None:
            subject = Subject.filter_by_id(topic.subject_id)
            return {
                "code": 200,
                "id": topic.id,
                "Topic Name": topic.topic_name,
                "Description": topic.topic_description,
                "Subject Name": subject.subject_name,
                "Videos": [
                    {
                        "Video ID": i.id,
                        "Video Name": i.video_name,
                        "Description": i.video_description,
                    }
                    for i in list(Video.select_all())
                    if i.topic_id == topic.id
                ],
                "Chatbots": [
                    {
                        "id": i.id,
                        "chatbot_name": i.chatbot_name,
                        "chatbot_version": i.chatbot_version,
                        "chatbot_access_code": i.chatbot_access_code,
                        "chatbot_uid": i.chatbot_uid,
                    }
                    for i in list(ChatBot.select_all())
                    if i.topic_id == topic.id
                ],
                "Meetings": [
                    {
                        "meeting_name": i.meeting_name,
                        "meeting_description": i.meeting_description,
                        "meeting_url": i.meeting_url,
                    }
                    for i in list(Meeting.select_all())
                    if i.topic_id == topic.id
                ],
            }
        return {"code": 404, "Message": "No Data Found"}, 404


class Topics(Resource):
    def get(self):
        topics = Topic.select_all()
        if topics != None:
            tops = []
            for topic in topics:
                subject = Subject.filter_by_id(topic.subject_id)
                tops.append(
                    {
                        "id": topic.id,
                        "Topic Name": topic.topic_name,
                        "Description": topic.topic_description,
                        "Subject Name": subject.subject_name,
                        "Videos": [
                            {
                                "Video ID": i.id,
                                "Video Name": i.video_name,
                                "Description": i.video_description,
                            }
                            for i in list(Video.select_all())
                            if i.topic_id == topic.id
                        ],
                        "Chatbots": [
                            {
                                "id": i.id,
                                "chatbot_name": i.chatbot_name,
                                "chatbot_version": i.chatbot_version,
                                "chatbot_access_code": i.chatbot_access_code,
                                "chatbot_uid": i.chatbot_uid,
                            }
                            for i in list(ChatBot.select_all())
                            if i.topic_id == topic.id
                        ],
                        "Meetings": [
                            {
                                "meeting_name": i.meeting_name,
                                "meeting_description": i.meeting_description,
                                "meeting_url": i.meeting_url,
                            }
                            for i in list(Meeting.select_all())
                            if i.topic_id == topic.id
                        ],
                    }
                )
            return {"code": 200, "Topics": tops}
        return {"code": 404, "Message": "No Data Found"}, 404


class Videos(Resource):
    def get(self, name):
        video = Video.filter_by_name(name)
        if video != None:
            return {
                "code": 200,
                "id": video.id,
                "Video Name": video.video_name,
                "Description": video.video_description,
            }
        return {"code": 404, "Message": "No Data Found"}, 404


class VideoRest(Resource):
    def get(self, id):
        video = Video.filter_by_id(int(id))
        if video != None:
            return {
                "code": 200,
                "Video ID": video.id,
                "Video Name": video.video_name,
                "Description": video.video_description,
            }
        return {"code": 404, "Message": "No Data Found"}, 404


class ChatBotIntentsRest(Resource):
    def get(self, id):
        chatbot = ChatBot.filter_by_id(id)
        if chatbot != None:
            return {
                "code": 200,
                "Chatbot ID": chatbot.id,
                "Chatbot Name": chatbot.chatbot_name,
                "Chatbot version": chatbot.chatbot_version,
                "Chatbot Access Code": chatbot.chatbot_access_code,
                "Intents": [
                    {
                        "Intent ID": i.id,
                        "Intent Name": i.intent_name,
                        "Intent Response": i.intent_response,
                    }
                    for i in list(Intent.select_all())
                    if i.chatbot_id == chatbot.id
                ],
            }
        return {"code": 404, "Message": "No Data Found"}, 404
class IntentRest(Resource):
    def get(self, name):
        intent = Intent.filter_by_name(name)
        if intent != None:
            return {
                "code": 200,
                "Intent ID": intent.id,
                "Response": intent.intent_response,
            }
        return {"code": 404, "Message": "No Data Found"}, 404