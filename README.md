### CS Search Engine https://cs-se-4e4c06e63a84.herokuapp.com

## ROADMAP:
:white_check_mark:1. Finish Heroku deploying with CI/CD:    ///Still need to finish deploying and fixing deploy bug(check debuging block) 

   1.1 Registration and research.
   
   1.2 Creating app.
   
   1.3 Deploying.
   
:white_check_mark:2. SteamAPI connecting:    ///Need to learn more about SteamAPI and viewall request to get all needed info 

   2.1 Research.
   
   2.2 Registration through SteamAPI.
   
   2.3 Parsing skins data.
   
   2.4 Parsing user data.
   
   
:white_check_mark:3. Database establishing:    ///After gettting along with API, i need to create a functionality to save&update mongodb database 

   3.1 Creating and researching.
   
   3.2 Basic functional to collect from json.
   
   3.3 Advenced functional to collect from api and convert inside app.
   
:white_check_mark:4. Creating store:   /// Store for a some functionality  
   4.1 Creating a page.
   
   4.2 Writing a store functional.
   
:white_check_mark:5. Creating a profile page: ///Profile page for user and functional invenrory 

   5.1 Creating a page.
   
   5.2 Writing a profile functional.
   
:white_check_mark:6. Creating a better and unique design: ///Task wasn`t finished on 100%, but what`s done is done 
   




## DEBUGING:
Need to deploy it at least somewhere. There is a problem with that, it`s just didn`t launching. Will optimize code and files, check it again. If still won`t be working, should thing about something else. Maybe swithcing to Jango, not sure yet.
Right now project is deployed to Heroku, just to be sure it`s working(spoiler:it is). 

## DEVBLOG:
This is student project associated with my hobby(CS:GO skins and its market). Right now its in early development stage, but it must be a kind of search engine/items  
database(aint sure about balance yet). 

28.03.23 It`s written on Python Flask framework + MongoDB. Should be deployed on Azure, but some problems was met, so right now it is deployed on heroku.

29-30.03.23 Learned a bit about Steam Api, used it to collect info about 100 market items, insert it into mongodb and configure to be shown on web-site.
Configure Gunicorn for Heroku deployment.

11.04.23 Ended resource limits for Heroku, but project was updated, so i think it will work better on other deployment services. Finished with steam auth info, trying dmarketAPI and working on better style

04.05.23 Established database view from dmarketAPI and getting info from api url. Decided to get only dmarketAPI info.

14.06.23 Changed app theme cause of functional blocks cause of API and other sources. Now it`s basic store with mongodb functional

21.06.23 Finished, not really enjoying with result, but i`m too done for futher work on this project. Too many problems P.S. In future, don`t choose project with theme, that you will enjoy working on, just don`t, you will say thank later.

## Local launch:
It`s is simple project, so there is no need for complicated launch. Just copy the rep and you`re almoste ready to go
You just need to provide connection string to your MongoDB
P.S. don`t forget to pip3 requirements.txt)
```sh
  def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #"mongodb+srv://UaroslavH:BV9caZNzBmBPiNYQ@csgoskinexplorer.patitvp.mongodb.net/test"
   CONNECTION_STRING = os.getenv('CONNECTION_STRING')
   client = MongoClient(CONNECTION_STRING)
   return client['CS_SE']

def get_database2():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   #"mongodb+srv://UaroslavH:BV9caZNzBmBPiNYQ@csgoskinexplorer.patitvp.mongodb.net/test"
   CONNECTION_STRING = os.getenv('CONNECTION_STRING')
   client = MongoClient(CONNECTION_STRING)
   return client['Users_info']
```
Then it will work on local server.

#Kind-of-diagram
https://lucid.app/lucidchart/af2486c7-f5b7-4467-8a79-a7b9c3e52007/edit?page=Qzx6eZss7Cns#
## Technology used:
1. Python: Python is a popular high-level programming language known for its simplicity and readability. It has a vast ecosystem of libraries and frameworks, making it versatile for various applications, including web development, data analysis, artificial intelligence, and more.

2. MongoDB: MongoDB is a NoSQL document-oriented database that provides high scalability, flexibility, and performance. It stores data in flexible, JSON-like documents, allowing for dynamic and evolving schemas. It is often used for handling large amounts of unstructured or semi-structured data.

3. Visual Studio Code: Visual Studio Code (VS Code) is a lightweight yet powerful source code editor developed by Microsoft. It supports a wide range of programming languages and provides features such as intelligent code completion, debugging, version control integration, and extensibility through plugins.

4. pymongo: pymongo is a Python library that provides a high-level interface for interacting with MongoDB databases. It simplifies the process of connecting to a MongoDB server, querying data, and performing CRUD (Create, Read, Update, Delete) operations on documents.

5. DMarketAPI: DMarketAPI is an API (Application Programming Interface) provided by DMarket, a platform for trading and exchanging in-game items and virtual assets. The API allows developers to access DMarket's features programmatically, such as retrieving item information, creating listings, and managing transactions.

6. Heroku: Heroku is a cloud platform that allows developers to deploy, manage, and scale applications easily. It supports various programming languages and provides a simple interface for deploying web applications without worrying about infrastructure management.

7. Gunicorn: Gunicorn is a Python HTTP server that is commonly used to deploy web applications. It acts as a middle layer between the web server and the application, handling incoming requests and distributing them to the application processes. Gunicorn is known for its simplicity, performance, and ability to handle multiple concurrent requests.

8. Steam API: Steam API is an application programming interface provided by Valve Corporation, the company behind the popular Steam gaming platform. It allows developers to access various features of the Steam platform, such as retrieving game information, user profiles, achievements, and integrating multiplayer functionality into their games.

9. Bootstrap: Bootstrap is a popular front-end framework that provides a collection of CSS and JavaScript components for building responsive and mobile-first web pages. It simplifies the process of creating attractive and consistent user interfaces by providing pre-designed elements, responsive grid systems, and customizable themes. Bootstrap helps developers save time and effort in designing and styling web applications.

Holovko Uaroslav
holovckouaroslav@gmail.com
https://t.me/Lowckick

## Lab 3:
Added ability to search and filter database content
<br>
Taras Rohulya:https://github.com/Tarasukk/Web;

Pull link:https://github.com/Tarasukk/WebProgrammingProject/commit/33909ade02d1c6ea585bf72fd8f496844bdd2ee6;

## Lab 4:
<br>
Vitalii Lylo
<br>
Github: https://github.com/VilaTiw/Immigration-Assistance-Application
<br>
Pull request: https://github.com/VilaTiw/Lowckick_WebProgrammingProject/pull/1
<br>
## Lab 4:
<br>
Taras Rohulia
<br>
Github: https://github.com/Tarasukk/Web;
<br>
Pull request: https://github.com/Tarasukk/WebProgrammingProject/pull/1
<br>
