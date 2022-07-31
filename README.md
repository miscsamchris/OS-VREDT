# OS VREDT : Open-Source Virtual Reality based EDucational Tool

## Introduction
OS VREDT is a Virtual Reality Application that allows Educators to use VR to stream Video content to students along with a dedicated chatbot for answering questions and clearing doubts.

OS VREDT is built with a loosely coupled architecture that enables us to create multiple end devices for viewing the VR Content.

It has been crafted with a dynamic data model that supports multiple types of syllabus and other non-academic materials.

## Motivation
The main motivation behind building this application is to create an application that can help me concentrate during self learning. I had to deal with a great deal of distractions while doing self study. I had the problem of going down the YouTube rabit-hole whenever I tried to look up some reference videos related to a topic.

I believe this application would be helpful for students, educational institutes and self-interest groups to create curated VR content that can help their audience learn the subject in and efficient way.

I also believe that this solution has a long way to go to reach its full potential and ability.

## Demo

#### Create Subject
https://vimeo.com/735180699

#### Create Topic
https://vimeo.com/735180733

#### Create Intent
https://vimeo.com/735181390

#### Create Video
https://vimeo.com/735180765

#### VR Application
https://vimeo.com/735181457

## Features

#### Customizability
OS VREDT can be customized to deliver content for a variety of subjects and topics

#### Loosely Coupled Design
The loosely couple design of OS VREDT make it so that we can create different clients for students and end users

#### Immersion
OS VREDT provides Immersion to the users to self learn in an efficient way

#### Novelty factor
OS VREDT is designed to be fun to use for users.

## Tech Stack

### Server
- HTML, CSS and JS - Frontend for web application
- Flask-Restful - Flask module for serving RESTful API
- Flask - Python based server
- MySQLDB - MySQL client for Python
- PlanetScale - Database Layer

### VR Application
- Google Cardboard - Open Sourced VR Development SDK
- C# and .Net Framework - Game Development Scripts
- Unity - Game Development Engine
- Android Library - Unity Encapsulated Android code

## Future Plans
- Implement a frontend Implementation for VR Meetings
- Implement a Data Analytics system  for individualized study plan
- Adding a quiz interface for assessment of learning

## Instructions

#### Python Server
1.  Navigate to `Server/TrainingTool/` and open __init__.py and update the PlanetScale connection details
![Init.py](https://cdn.hashnode.com/res/hashnode/image/upload/v1659275132795/LNgAM9-Xy.png)
2. Navigate to `Server/TrainingTool/Topics/` and open views.py and update the Authorization token
![views.py](https://cdn.hashnode.com/res/hashnode/image/upload/v1659275500080/a25Owoviq.png)
3. Navigate to `Server` and open app.py and update the host name with your IP address.
![app.py](https://cdn.hashnode.com/res/hashnode/image/upload/v1659275624070/CnaiuBaLh.png)
4. Open command prompt and navigate to `Server` and run the following commands
```
python init_db.py
python app.py
```


#### VR Application
1. Open the Unity Project and configure the Visual Studio Project Settings.

2. Update the URL to the Hostname of the server with the path in all of the scripts
![URL](https://cdn.hashnode.com/res/hashnode/image/upload/v1659275921171/6YsC29u7g.png)
3. Open the `File>Build Settings` and click on the `Build and Run` after connecting the mobile device
![Build&Run](https://cdn.hashnode.com/res/hashnode/image/upload/v1659276454703/-p_RjhFPY.png)
4. Save the apk file for distribution and build the file.
![saveapk](https://cdn.hashnode.com/res/hashnode/image/upload/v1659277597620/sVMc150CR.png)

## Important Links
- [Live Demo](https://osvredt.herokuapp.com)
- [VR Application](https://drive.google.com/file/d/1PTVKx6YzUMpnuIQTWSZqCaeo_H4aGv4_/view?usp=sharing)
- [GitHub Repository](https://github.com/miscsamchris/OS-VREDT)

## Conclusion
To conclude, I would like to thank the Hashnode and PlanetScale team to provide me the opportunity for me to work on something I feel very attached to. It was an absolute delight working with PlanetScale's serverless MySQL Database Platform.
