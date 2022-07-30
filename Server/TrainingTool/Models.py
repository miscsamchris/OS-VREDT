import sys
from TrainingTool import db


class Subject:
    __tablename__ = "Subjects"
    id = 0
    subject_name = ""

    def __init__(self, name=""):
        self.subject_name = name

    def initialize(self, id, name):
        self.id = id
        self.subject_name = name

    def filter_by_name(name):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Subjects where subject_name=%s""", (name,))
        data = cur.fetchone()
        subject = Subject()
        subject.initialize(*data)
        db.close()
        return subject

    def filter_by_id(id):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Subjects where id=%s""", (id,))
        data = cur.fetchone()
        subject = Subject()
        subject.initialize(*data)
        db.close()
        return subject

    def select_all():
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Subjects """)
        data = cur.fetchall()
        subjects = []
        for i in data:
            subject = Subject()
            subject.initialize(*i)
            subjects.append(subject)
        db.close()
        return subjects

    def insert(self):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute(
            """INSERT INTO Subjects (subject_name) VALUES (%s)""", (self.subject_name,)
        )
        db_session.commit()
        data=cur.execute("""SELECT LAST_INSERT_ID()""")
        data=cur.fetchone()
        print(data,file=sys.stderr)
        self.id=data[0]
        db.close()
    def __repr__(self):
        return f"{self.subject_name}"


class Topic:
    __tablename__ = "Topics"
    id = 0
    topic_name = ""
    subject_id = 0
    topic_description = ""

    def __init__(self, topic_name="", subject_id=0, topic_description=""):
        self.topic_name = topic_name
        self.subject_id = subject_id
        self.topic_description = topic_description

    def subject_from_topic(self):
        if self.subject_id:
            subject = Subject.filter_by_id(self.subject_id)
        return subject

    def initialize(self, id, topic_name, subject_id, topic_description):
        self.id = id
        self.topic_name = topic_name
        self.subject_id = subject_id
        self.topic_description = topic_description

    def filter_by_name(name):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Topics where topic_name=%s""", (name,))
        data = cur.fetchone()
        topic = Topic()
        topic.initialize(*data)
        db.close()
        return topic

    def filter_by_id(id):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Topics where id=%s""", (id,))
        data = cur.fetchone()
        topic = Topic()
        topic.initialize(*data)
        db.close()
        return topic

    def select_all():
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Topics """)
        data = cur.fetchall()
        topics = []
        for i in data:
            topic = Topic()
            topic.initialize(*i)
            topics.append(topic)
        db.close()
        return topics

    def insert(self):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute(
            """INSERT INTO Topics (topic_name,subject_id,topic_description) VALUES (%s,%s,%s)""",
            (
                self.topic_name,
                self.subject_id,
                self.topic_description,
            ),
        )
        db_session.commit()
        data=cur.execute("""SELECT LAST_INSERT_ID()""")
        data=cur.fetchone()
        print(data,file=sys.stderr)
        self.id=data[0]
        db.close()

    def __repr__(self):
        return f"{self.topic_name}"


class Video:
    __tablename__ = "Videos"
    id = 0
    video_name = ""
    topic_id = 0
    video_description = ""
    video_url = ""
    video_path = ""

    def __init__(self, video_name="", topic_id="", video_description="", video_url=""):
        self.video_name = video_name
        self.topic_id = topic_id
        self.video_description = video_description
        self.video_url = video_url
        self.video_path = ""

    def topic_from_video(self):
        if self.subject_id:
            topic = Topic.filter_by_id(self.topic_id)
        return topic

    def initialize(
        self, id, video_name, topic_id, video_description, video_url, video_path
    ):
        self.id = id
        self.video_name = video_name
        self.topic_id = topic_id
        self.video_description = video_description
        self.video_url = video_url
        self.video_path = video_path

    def filter_by_name(name):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Videos where video_name=%s""", (name,))
        data = cur.fetchone()
        video = Video()
        video.initialize(*data)
        db.close()
        return video

    def filter_by_id(id):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Videos where id=%s""", (id,))
        data = cur.fetchone()
        video = Video()
        video.initialize(*data)
        db.close()
        return video

    def select_all():
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Videos """)
        data = cur.fetchall()
        videos = []
        for i in data:
            video = Video()
            video.initialize(*i)
            videos.append(video)
        db.close()
        return videos

    def insert(self):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute(
            """INSERT INTO Videos (video_name,topic_id,video_description,video_url,video_path) VALUES (%s,%s,%s,%s,%s)""",
            (
                self.video_name,
                self.topic_id,
                self.video_description,
                self.video_url,
                self.video_path,
            ),
        )
        db_session.commit()
        data=cur.execute("""SELECT LAST_INSERT_ID()""")
        data=cur.fetchone()
        print(data,file=sys.stderr)
        self.id=data[0]
        db.close()
    def __repr__(self):
        return f"{self.video_name} : {self.video_path}"


class Meeting:
    __tablename__ = "Meetings"
    id = 0
    meeting_name = ""
    topic_id = 0
    meeting_description = ""
    meeting_url = ""

    def __init__(
        self, meeting_name="", topic_id="", meeting_description="", meeting_url=""
    ):
        self.meeting_name = meeting_name
        self.topic_id = topic_id
        self.meeting_description = meeting_description
        self.meeting_url = meeting_url

    def initialize(self, id, meeting_name, topic_id, meeting_description, meeting_url):
        self.id = id
        self.meeting_name = meeting_name
        self.topic_id = topic_id
        self.meeting_description = meeting_description
        self.meeting_url = meeting_url

    def filter_by_name(name):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Meetings where meeting_name=%s""", (name,))
        data = cur.fetchone()
        meet = Meeting()
        meet.initialize(*data)
        db.close()
        return meet

    def filter_by_id(id):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Meetings where id=%s""", (id,))
        data = cur.fetchone()
        meet = Meeting()
        meet.initialize(*data)
        db.close()
        return meet

    def select_all():
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Meetings """)
        data = cur.fetchall()
        meets = []
        for i in data:
            meet = Topic()
            meet.initialize(*i)
            meets.append(meet)
        db.close()
        return meets

    def insert(self):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute(
            """INSERT INTO Meetings (meeting_name,topic_id,meeting_description,meeting_url) VALUES (%s,%s,%s,%s)""",
            (
                self.meeting_name,
                self.topic_id,
                self.meeting_description,
                self.meeting_url,
            ),
        )
        db_session.commit()
        data=cur.execute("""SELECT LAST_INSERT_ID()""")
        data=cur.fetchone()
        print(data,file=sys.stderr)
        self.id=data[0]
        db.close()

    def __repr__(self):
        return f"{self.meeting_name} : {self.meeting_url}"


class ChatBot:
    __tablename__ = "ChatBots"
    id = 0
    chatbot_name = ""
    chatbot_version = ""
    chatbot_access_code = ""
    chatbot_uid = ""
    topic_id = 0

    def __init__(
        self,
        chatbot_name="",
        chatbot_version="",
        chatbot_access_code="",
        chatbot_uid="",
        topic_id="",
    ):
        self.chatbot_name = chatbot_name
        self.chatbot_version = chatbot_version
        self.chatbot_access_code = chatbot_access_code
        self.chatbot_uid = chatbot_uid
        self.topic_id = topic_id

    def initialize(
        self,
        id,
        chatbot_name,
        chatbot_version,
        chatbot_access_code,
        chatbot_uid,
        topic_id,
    ):
        self.id = id
        self.chatbot_name = chatbot_name
        self.chatbot_version = chatbot_version
        self.chatbot_access_code = chatbot_access_code
        self.chatbot_uid = chatbot_uid
        self.topic_id = topic_id

    def filter_by_name(name):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from ChatBots where chatbot_name=%s""", (name,))
        data = cur.fetchone()
        chatbot = ChatBot()
        chatbot.initialize(*data)
        db.close()
        return chatbot

    def filter_by_id(id):
        db_session=db.connect()
        cur = db_session.cursor()
        print(id,)
        cur.execute("""SELECT * from ChatBots where id=%s""", (id,))
        data = cur.fetchone()
        chatbot = ChatBot()
        chatbot.initialize(*data)
        db.close()
        return chatbot

    def select_all():
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from ChatBots """)
        data = cur.fetchall()
        chatbots = []
        for i in data:
            chatbot = ChatBot()
            chatbot.initialize(*i)
            chatbots.append(chatbot)
        db.close()
        return chatbots

    def insert(self):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute(
            """INSERT INTO ChatBots (chatbot_name,chatbot_version,chatbot_access_code,chatbot_uid,topic_id) VALUES (%s,%s,%s,%s,%s)""",
            (
                self.chatbot_name,
                self.chatbot_version,
                self.chatbot_access_code,
                self.chatbot_uid,
                self.topic_id,
            ),
        )
        db_session.commit()
        data=cur.execute("""SELECT LAST_INSERT_ID()""")
        data=cur.fetchone()
        print(data,file=sys.stderr)
        self.id=data[0]
        db.close()

    def __repr__(self):
        return f"{self.chatbot_name} : {self.chatbot_uid}"


class Intent:
    __tablename__ = "Intents"
    id = 0
    intent_name = ""
    intent_uid = ""
    chatbot_id = 0
    intent_response = ""

    def __init__(
        self, intent_name="", intent_uid="", chatbot_id="", intent_response=""
    ):
        self.intent_name = intent_name
        self.intent_uid = intent_uid
        self.chatbot_id = chatbot_id
        self.intent_response = intent_response

    def initialize(self, id, intent_name, intent_uid, chatbot_id, intent_response):
        self.id = id
        self.intent_name = intent_name
        self.intent_uid = intent_uid
        self.chatbot_id = chatbot_id
        self.intent_response = intent_response

    def filter_by_name(name):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Intents where intent_name=%s""", (name,))
        data = cur.fetchone()
        intent = Intent()
        intent.initialize(*data)
        db.close()
        return intent

    def filter_by_id(id):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Intents where id=%s""", (id,))
        data = cur.fetchone()
        intent = Intent()
        intent.initialize(*data)
        db.close()
        return intent

    def select_all():
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute("""SELECT * from Intents """)
        data = cur.fetchall()
        intents = []
        for i in data:
            intent = Intent()
            intent.initialize(*i)
            intents.append(intent)
        db.close()
        return intents

    def insert(self):
        db_session=db.connect()
        cur = db_session.cursor()
        cur.execute(
            """INSERT INTO Intents (intent_name,intent_uid,chatbot_id,intent_response) VALUES (%s,%s,%s,%s)""",
            (
                self.intent_name,
                self.intent_uid,
                self.chatbot_id,
                self.intent_response,
            ),
        )
        db_session.commit()
        data=cur.execute("""SELECT LAST_INSERT_ID()""")
        data=cur.fetchone()
        print(data,file=sys.stderr)
        self.id=data[0]
        db.close()

    def __repr__(self):
        return f"{self.intent_name} : {self.intent_uid}"
