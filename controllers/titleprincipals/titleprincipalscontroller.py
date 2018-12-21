from root import application

@application.route("/titleprincipals", methods=["GET"])
def titleprincipals_home():
    return "Welcome to Title Principals API"