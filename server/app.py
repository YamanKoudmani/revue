<<<<<<< HEAD
"""
GUIDE: This defines the entry point to the flask app.
"""
import config
import os

from datetime import date
from flask import Flask, jsonify, send_from_directory

from flask.json import JSONEncoder
from flask_cors import CORS

class CustomJSONEncoder(JSONEncoder):
    """Use ISO 8601 for dates"""

    def default(self, obj):  # noqa: E0202
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.config["SECRET_KEY"] = config.flask_secret_key

# GUIDE: Cross-Origin Resource Sharing is a mechanism used by servers to tell the browser which other servers the browser should trust for this site.
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
CORS(app)


# GUIDE: This is how we tell flask to respond to a request on a specific url
# This particular instance responds to /api/file/filename. The last segment, filename, is turned into a string and passed as an argument to the function
# The @ syntax is called a function decorator. @app.route() is a function that takes another function as an argument and returns a modified function
# This is an advanced python feature that can be a lot of fun to waste time with.
# Flask makes great use of function decorators to attach functions to server responses/behaviors
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route
@app.route("/api/file/<string:filename>")
def images_get(filename):
    return send_from_directory(config.image_upload_folder, filename)


from views.authentication import *  # noqa
from views.posts import *  # noqa
from views.subvues import *  # noqa
from views.users import *  # noqa

import errors  # noqa


# GUIDE: here are functions to respond to various server errors. Note the use of decorators.
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": "API endpoint not found"
    }), 404


@app.errorhandler(500)
@app.errorhandler(405)
def internal_server_error(e):
    return jsonify({
        "error": "Internal server error"
    }), 500


@app.errorhandler(413)
def request_entity_too_large(e):
    return jsonify({
        "error": "To large (max. 1 MB)"
    }), 413


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
=======
"""
GUIDE: This defines the entry point to the flask app.
"""
import config
import os

from datetime import date
from flask import Flask, jsonify, send_from_directory
from flask.json import JSONEncoder
from flask_cors import CORS
from models import Locations, Services, Reviews
class CustomJSONEncoder(JSONEncoder):
    """Use ISO 8601 for dates"""

    def default(self, obj):  # noqa: E0202
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.config["SECRET_KEY"] = config.flask_secret_key
# GUIDE: Cross-Origin Resource Sharing is a mechanism used by servers to tell the browser which other servers the browser should trust for this site.
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
CORS(app)


# GUIDE: This is how we tell flask to respond to a request on a specific url
# This particular instance responds to /api/file/filename. The last segment, filename, is turned into a string and passed as an argument to the function
# The @ syntax is called a function decorator. @app.route() is a function that takes another function as an argument and returns a modified function
# This is an advanced python feature that can be a lot of fun to waste time with.
# Flask makes great use of function decorators to attach functions to server responses/behaviors
# https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route
@app.route("/api/file/<string:filename>")
def images_get(filename):
    return send_from_directory(config.image_upload_folder, filename)


from views.authentication import *  # noqa
from views.posts import *  # noqa
from views.subvues import *  # noqa
from views.users import *  # noqa

import errors  # noqa

# GUIDE: here are functions to respond to various server errors. Note the use of decorators.
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": "API endpoint not found"
    }), 404


@app.errorhandler(500)
@app.errorhandler(405)
def internal_server_error(e):
    return jsonify({
        "error": "Internal server error"
    }), 500


@app.errorhandler(413)
def request_entity_too_large(e):
    return jsonify({
        "error": "To large (max. 1 MB)"
    }), 413

@app.route("/api/yay")
def demo():
    #Food Locations
    Cafe = Locations(name = "Hard Knox Cafe", reviewList = None).save()
    Gizmo = Locations(name = "Gizmo", reviewList = None).save()
    GrabnGo = Locations(name = "Grab n Go", reviewList = None).save()
    Outpost = Locations(name = "Outpost Express (C-Store)", reviewList = None).save()
    foodLocations = {Cafe, Gizmo, GrabnGo, Outpost}
    #Housing Locations
    Seymour_Hall = Locations(name = "Seymour Hall", reviewList = None).save()
    Post_Hall = Locations(name = "Post Hall", reviewList = None).save()
    Griffith = Locations(name = "Griffith-Longden-Drew-Simmonds (Four-Name)", reviewList = None).save()
    Raub_Sellew_Hall = Locations(name = "Raub-Sellew Hall", reviewList = None).save()
    Hamblin_Hall = Locations(name = "Hamblin Hall", reviewList = None).save()
    Sherwin_Neifert_Hall = Locations(name = "Sherwin-Neifert Hall", reviewList = None).save()
    Williston_Hall = Locations(name = "Williston Hall", reviewList = None).save()
    Exec_Apartments = Locations(name = "Exec Apartments", reviewList = None).save()
    Tomkins_Apartments = Locations(name = "Tomkins Apartments", reviewList = None).save()
    Townhouses = Locations(name = "Townhouses", reviewList = None).save()
    housingLocations = {Seymour_Hall, Post_Hall, Griffith, Raub_Sellew_Hall,Hamblin_Hall,Sherwin_Neifert_Hall,Williston_Hall,Exec_Apartments,Tomkins_Apartments,Townhouses}
    #IT Locations
    Burkhardtlab = Locations(name = "Burkhardt Lab", reviewList = None).save()
    CAT = Locations(name = "Caterpillar Classroom (CAT)", reviewList = None).save()
    Digital_Studio = Locations(name = "Sparks Digital Studio (WAC)", reviewList = None).save()
    Stellyeslab = Locations(name = "Stellyes Lab", reviewList = None).save()
    Founderslab = Locations(name = "Founders Lab", reviewList = None).save()
    ITLocations = {Burkhardtlab, CAT, Digital_Studio, Stellyeslab, Founderslab}
    #Physical Activites
    Andrew_Fitness = Locations(name = "E & L Andrew fitness center", reviewList = None).save()
    Fieldhouse = Locations(name = "Fieldhouse", reviewList = None).save()
    Basketball = Locations(name = "Basketball", reviewList = None).save()
    Tennis_court = Locations(name = "Tennis court", reviewList = None).save()
    Swimming_pool = Locations(name = "Swimming pool", reviewList = None).save()
    Soccer_Field = Locations(name = "Soccer field", reviewList = None).save()
    Knosher_Bowl = Locations(name = "Knosher Bowl", reviewList = None).save()
    physicalLocations = {Andrew_Fitness, Fieldhouse, Basketball, Tennis_court, Swimming_pool, Soccer_Field, Knosher_Bowl}
    #Library Locations    
    Seymour = Locations(name = "Seymour", reviewList = None).save()
    SMClibrary = Locations(name = "SMC Library", reviewList = None).save()
    libraryLocations = {Seymour, SMClibrary}
    #Creativity 
    CFA_dance_studio = Locations(name = "CFA: Dance Studio", reviewList = None).save()
    CFA_paino_rooms = Locations(name = "CFA: Piano Rooms", reviewList = None).save()
    Harbach_Theatre = Locations(name = "Harbach Theatre", reviewList = None).save()
    Kresge = Locations(name = "Kresge Recital Hall", reviewList = None).save()
    Round_Room = Locations(name = "CFA: Round Room", reviewList = None).save()
    WAC_print_making = Locations(name = "WAC: Print Making Studio", reviewList = None).save()
    WAC_drawing = Locations(name = "WAC: Drawing Studio", reviewList = None).save()
    WAC_photo_printer = Locations(name = "WAC: Photo Printer", reviewList = None).save()
    creativityLocations = {CFA_dance_studio, CFA_paino_rooms, Harbach_Theatre, Kresge, Round_Room, WAC_print_making, WAC_drawing, WAC_photo_printer}
    #Postal
    Mail = Locations(name = "Mail Room", reviewList = None).save()
    mailLocations = {Mail}
    #Health
    HealthS = Locations(name = "Health services", reviewList = None).save()
    HealthC = Locations(name = "Health Counseling", reviewList = None).save()
    healthLocations = {HealthS, HealthC}
    #Entertainment
    Taylor = Locations(name = "Taylor Lounge", reviewList = None).save()
    entertainmentLocations = {Taylor}

    #SERVICES
    FoodServices = Services(name = "Food", description = "There are a variety of meal services around Knox. Below you'll find detailed information on the locations offered:", locations = foodLocations).save()
    HousingServices = Services(name = "Housing", description = "Knox offers a plethora of housing options for students. Below you'll find detailed information on the locations offered:", locations = housingLocations).save()
    ITServices = Services(name = "IT Services", description = "We have multiple Computer Labs on campus here at Knox. Below you'll find detaled information on the locations offered:", locations = ITLocations).save()
    PhysicalServices = Services(name = "Physical Services", description = "We have Physical Services on campus for all our athletes and help the rest of keep in shape! Below you'll find detaled information on the locations offered:", locations = physicalLocations).save()
    LibaryServices = Services(name = "Libraries", description = "We have 2 major libraries here at Knox that are excellent resources. Below you'll find more details about our incredible Library servies:", locations = libraryLocations).save()
    MailServices = Services(name = "Mail Services", description = "All your mail needs are covered in the Mail Room, where you can send and recieve mail and packages", locations = mailLocations).save()
    HealthServices = Services(name = "Health Services", description = "Knox College provides primary health care services to all registered students.", locations = healthLocations).save()
    CreativityServices = Services(name = "Creativity", description = "There are multiple creative studios and locations on our campus. Below you'll find more details on these spaces:", locations = creativityLocations).save()
    EntertainmentServices = Services(name = "Entertainment!", description = "Tired of studying? We might have just what you need:", locations = entertainmentLocations).save()



    return jsonify({
        "error": "The code completed successfully (and that's a bad thing)"
    }), 500

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)

>>>>>>> development
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)