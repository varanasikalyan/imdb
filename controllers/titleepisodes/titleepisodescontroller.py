from root import application

@application.route("/titleepisodes", methods=["GET"])
def titleepisodes_home():
    return "Welcome to Title Episodes API"