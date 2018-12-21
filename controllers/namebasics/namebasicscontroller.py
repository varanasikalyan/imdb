from root import application

@application.route("/namebasics", methods=["GET"])
def namebasics_home():
    return "Welcome to Names API"