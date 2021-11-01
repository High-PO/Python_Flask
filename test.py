from flask import Flask, render_template, jsonify, Request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

# @app.route("/")
# def index():
#     return render_template('./index.html')
    
@api.route("/getapi")
class GetApi(Resource):
    def get(self):
        return {"Name":"HelloWorld"}

@api.route("/index")
class index(Resource):
    def get(self):
        return render_template('./index.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=80,debug=True)