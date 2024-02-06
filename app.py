from flask import Flask
from view import views
app = Flask(__name__, static_url_path='/static', static_folder='static')

#initalizes ur flask application and can be used for easy application run 

app.register_blueprint(views, url_prefix="")


#now that the website has been initialized we can add views and pages for example a home page or a 'about me' page. this is done in views.py

#since flask is already initialized you can run application with: 
if __name__ == "__main__":
    app.run(debug = True, port = 8000)