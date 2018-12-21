from root import application

@application.route("/titleakas", methods=["GET"])
def titleakas_home():
    return "Welcome to Title AKAS API"