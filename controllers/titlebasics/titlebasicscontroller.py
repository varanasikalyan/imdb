from root import application

@application.route("/titlebasics", methods=["GET"])
def titlebasics_home():
    return "Welcome to Title Basics API"