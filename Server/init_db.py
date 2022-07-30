from operator import imod
from TrainingTool import app, db


def create_all():
    try:
        
        cur = db.connect().cursor()
        cur.execute(
            """CREATE TABLE Subjects(
                        id int AUTO_INCREMENT,
                        subject_name Text,PRIMARY KEY (id))"""
        )
        cur.execute(
            """CREATE TABLE Topics(
                        id int AUTO_INCREMENT,
                        topic_name Text,
                        subject_id int,
                        topic_description Text,
                        PRIMARY KEY (id))"""
        )
        cur.execute(
            """CREATE TABLE Videos(
                        id int AUTO_INCREMENT,
                        video_name Text,
                        topic_id int,
                        video_description Text,
                        video_url Text,
                        video_path Text,PRIMARY KEY (id))"""
        )
        cur.execute(
            """CREATE TABLE Meetings(
                        id int AUTO_INCREMENT,
                        meeting_name Text,
                        topic_id int,
                        meeting_description Text,
                        meeting_url Text,PRIMARY KEY (id))"""
        )
        cur.execute(
            """CREATE TABLE ChatBots(
                        id int AUTO_INCREMENT,
                        chatbot_name Text,
                        chatbot_version Text,
                        chatbot_access_code Text,
                        chatbot_uid Text,
                        topic_id int,PRIMARY KEY (id))"""
        )
        cur.execute(
            """CREATE TABLE Intents(
                        id int AUTO_INCREMENT,
                        intent_name Text,
                        intent_uid Text,
                        chatbot_id int,
                        intent_response Text,PRIMARY KEY (id))"""
        )
        db.close()
    except Exception as e:
        print(e)


def drop_all():
    try:
        cur = db.connect().cursor()
        cur.execute("""DROP TABLE Subjects""")
        cur.execute("""DROP TABLE Topics""")
        cur.execute("""DROP TABLE Videos""")
        cur.execute("""DROP TABLE Meetings""")
        cur.execute("""DROP TABLE ChatBots""")
        cur.execute("""DROP TABLE Intents""")
        db.close()
    except Exception as e:
        print(e)


drop_all()
create_all()
from TrainingTool.Models import Subject

print(Subject.select_all())
