from root import application

@application.route("/titlecrew", methods=["GET"])
def titlecrew_home():
    return "Welcome to Title Crew API"