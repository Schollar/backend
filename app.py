from flask import Flask, request, Response
import dbinteractions as db
import json
import traceback
import sys

app = Flask(__name__)


@app.get("/api/line")
def get_line():
    try:
        lines, success = db.get_lines()
        if(success):
            lines_json = json.dumps(lines, default=str)
            return Response(lines_json, mimetype="application/json", status=200)
        else:
            return Response("Lines Failure", mimetype="plain/text", status=422)
    except:
        traceback.print_exc()
        print("DO BETTER ERROR CATCHING")
        return Response("Data Error", mimetype="text/plain", status=400)


@app.post("/api/line")
def post_line():
    id, success = None, False
    try:
        line = request.json['content']
        id, success = db.make_line(line)
    except:
        traceback.print_exc()
        print("DO BETTER ERROR CATCHING")
        return Response("Data Error", mimetype="text/plain", status=400)
    if(success):
        return Response(f"Post {id} Success!", mimetype="plain/text", status=201)
    else:
        return Response("Post Failure", mimetype="plain/text", status=422)


if(len(sys.argv) > 1):
    mode = sys.argv[1]
else:
    print("You must pass a mode to run this python script. Either testing or production. For example:")
    print("python app.py testing")
    exit()

if(mode == "testing"):
    print("Running in testing mode!")
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif(mode == "production"):
    print("Running in production mode")
    import bjoern  # type: ignore
    bjoern.run(app, "0.0.0.0", 5005)
else:
    print("Please run with either testing or production. Example:")
    print("python app.py production")
