import flask
import json
import traceback

# We're going to mock this one since the save package doesn't behave as Codility specifies
#from save import save

app = flask.Flask(__name__)


def save(json_object):
    return json_object

@app.route("/users", methods=["POST"])
def users():
    # Verify that the payload is JSON
    if flask.request.is_json:
        try:
            json_data = flask.request.get_json()
        except:
            return "Payload must be JSON", 400

        # Verify that the name and age attributes exist in the JSON payload
        if 'name' not in json_data or 'age' not in json_data:
            return "Payload must include the 'name' and 'age' attributes", 400

        name = json_data['name']
        age = json_data['age']

        # Verify that name isn't longer than 32 characters
        if len(name) > 32:
            return "Name cannot be longer than 32 characters", 400

        # Verify that age is a number (int)
        if not isinstance(age, int):
            return "Age must be a number", 400

        # Verify that age is over 16
        if age < 16:
            return "Age cannot be less than 16", 400

        return_object = save(json_data)

        return flask.jsonify(return_object), 201
    else:
        return "Payload must be JSON", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0')
