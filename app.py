# 1. import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# 2. Inisiasi Object
app = Flask(__name__)

# 3. inisiasi object flask_restful
api = Api(app)

# 4. inisiasi object flask_cors
CORS(app)

#-- Global Variable to store data
identitas = {} #JSON 

# 5. membuat class Resource
class ContohResource(Resource):
    
# metode get dan post
 def get(self):
        #response = {"msg": "Hallo dunia, ini app restful pertama ku"}
  return identitas
    
 def post(self):
  nama = request.form["nama"]
  umur = request.form["umur"]
  identitas["nama"] = nama
  identitas["umur"] = umur
  response = {"msg" : "Data berhasil dimasukan!"}
  return response

# 6. setup resource nya
     # URL
api.add_resource(ContohResource,"/api", methods=["GET","POST"])

if __name__ == "__main__":
 app.run(debug=True, port=5005)