from flask import Blueprint, render_template, request, jsonify, redirect, url_for, send_from_directory
import os

# Use the 'static' folder for image uploads
UPLOAD_FOLDER = "static/images"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the uploaded file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

views = Blueprint("views", __name__)
test = Blueprint("test", __name__)


@views.route("/")
def home():
    return render_template("index.html")
    #if you say return render_template("index.html", name = "Phoebe") (then refer to index.html)

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/resume")
def resume():
    return render_template("resume.html")

@views.route("/apps")
def apps():
    return render_template("apps.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")

@views.route("/blender")
def blender():
    return render_template("blender.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")
#this is show a new page if you type in /test

#@views.route("/profile/<username>")
#def profile(username):
    #return render_template("index.html", name = username)
    
# eg. url/views/profile?name= 
#this is called a query parameter (where you pass in a query in the link)
#import something from flask called request

#def profile(username):
    #return render_template("index.html", name = username)
    #arg = request.args
    #(can be used as a dictionary to acess any query parameters)
    #eg names = args.get('name')
    #return render_template("index.html", name = name)
@views.route("/tennis_image")
def tennis_image():
    return render_template("tennis.html")

@views.route("/image_clickable")
def image_clickable():
    return render_template("image_clickable.html")

@views.route("/image_clickable2")
def image_clickable_two():
    return render_template("image_clickable2.html")

@views.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@views.route("/json")
def get_json():
    return jsonify ({'name':"phoebe"})

@views.route("/mystery_button")
def mystery_button():
    return render_template("mystery_button.html")

@views.route("/test")
def testing():
    return render_template("test.html")
#getting json data
#acessing json sent to this route
@views.route("/data")
#someones going to send data in a json format 
def get_data():
    data = request.json
    return jsonify(data)

#redirect to a new page 

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for('view.home'))
    #return redirect(url_for'views.get_json')
    #will redirect you to the get_json route



