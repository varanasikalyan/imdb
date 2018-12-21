from root import application

@application.route("/titleratings", methods=["GET"])
def titleratings_home():
    return "Welcome to Title Ratings API"