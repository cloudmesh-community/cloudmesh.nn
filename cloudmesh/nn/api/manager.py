from flask import jsonify
import connexion

# Create the application instance
location = "./../../../"
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("spec/nn.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Your 2019 Project Has begun!"}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


class Manager(object):

    def __init__(self):
        print("init {name}".format(name=self.__class__.__name__))

    def list(self, parameter):
        print("list", parameter)
