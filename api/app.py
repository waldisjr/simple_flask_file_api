from flask import Flask, request
from file_funcs import FileFuncs

# initialize Flask instance
app = Flask(__name__)

# initialize instance with hardcoded filename
file = FileFuncs("data.txt")


# create handler for 404 error
@app.errorhandler(404)
def page_not_found(e):
    return {
               "result": False,
               "message": "Not Found"
           }, 404


# create index route for information
@app.route("/", methods=["GET"])
def index():
    return {
        "result": True,
        "message": "Basic files API. For documentation contact creator: t.me/waldis_jr"
    }


# create index route for information
@app.route("/file/", methods=["POST", "GET", "DELETE", "PATCH"])
def file_methods():
    if request.method == "GET":
        return {
                   "result": True,
                   "file_content": file.get_file_content()
               }, 200

    elif request.method == "DELETE":
        file.clear_file()
        return {
                   "result": True,
                   "message": "File was cleared."
               }, 200

    else:
        try:
            content = request.args["new_content"]
        except KeyError:
            return {
                       "result": False,
                       "message": "Incorrect request structure. Check documentation."
                   }, 400
        if request.method == "POST":
            file.replace_file_content(content)
            return {
                       "result": True,
                       "message": "File content was rewritten."
                   }, 200
        elif request.method == "PATCH":
            file.add_content_to_file(content)
            return {
                       "result": True,
                       "message": "New content was added to file."
                   }, 200


# enable debug (only if runs as main)
if __name__ == '__main__':
    app.run(debug=True)
