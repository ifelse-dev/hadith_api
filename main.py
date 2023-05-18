from flask import Flask, Response
import json
import random


app = Flask(__name__)

with open('hadith.db') as f:
    list = json.load(f)

@app.route("/hadith", methods=['GET'])
@app.route("/hadith/", methods=['GET'])
def get_hadith():
    hadith_index = random.randint(0, len(list)-1)
    choiseHadith_ar = list[hadith_index]["hadith_ar"]
    choiseHadith_fr = list[hadith_index]["hadith_fr"]


    return json.dumps({"hadith_ar": choiseHadith_ar,
                       "hadith_fr": choiseHadith_fr})

@app.route("/hadith/<id>", methods=['GET'])
@app.route("/hadith/<id>/", methods=['GET'])
def get_hadith_by_id(id):
    choiseHadith_ar = list[int(id)%len(list)]["hadith_ar"]
    choiseHadith_fr = list[int(id)%len(list)]["hadith_fr"]

    res = json.dumps({"hadith_ar": choiseHadith_ar,
                       "hadith_fr": choiseHadith_fr})  
    return  Response(res, mimetype='json/application')

app.run(debug=True)
print("Start api...")