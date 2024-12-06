from flask import Flask, render_template, jsonify, request

from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain
#from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality
from uspstf_knowledgebase import USPSTF_KnowledgeBase

app = Flask(__name__)



@app.route("/")
def index():
    # Render the HTML page with patient data
    return render_template("index.html")

@app.route("/get_result", methods=["POST"])
def get_result():
    patient_data = request.get_json()


    result = USPSTF_KnowledgeBase.calculate_for_all(patient_data)
    
    result["pregnancy_healthy_weight_gain"]=pregnancy_healthy_weight_gain.get_pregnancy_healthy_weight_gain_recommendation(pregnant=patient_data["pregnant"])
    #result["prevent_obesity_morbidity_mortality"]=prevent_obesity_morbidity_mortality.get_obesity_recommendation(age=patient_data["age"],bmi=patient_data["bmi"])
 
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
    
# export FLASK_APP=sdk_demo.app:app 
# flask run 
 