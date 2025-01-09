import os
from flask import Flask, render_template, jsonify, request

from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain
from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality
from abdominal_aortic_aneurysm_screening import abdominal_aortic_aneurysm_screening
from cardiovascular_prevention_diet_activity import cardiovascular_prevention_diet_activity
from cardiovascular_prevention_statin_use import cardiovascular_prevention_statin_use
from hypertension_screening import hypertension_screening
from diabetes_screening import diabetes_screening
from high_body_mass_index import high_body_mass_index

app = Flask(__name__)



@app.route("/")
def index():
    # Render the HTML page with patient data
    return render_template("index.html")

@app.route("/get_result", methods=["POST"])
def get_result():
    patient_data = request.get_json()


    result = {}
    result["abdominal_aortic_aneurysm_screening"]=abdominal_aortic_aneurysm_screening.execute(patient_data)
    result["cardiovascular_prevention_diet_activity"]=cardiovascular_prevention_diet_activity.execute(patient_data)
    result["cardiovascular_prevention_statin_use"]=cardiovascular_prevention_statin_use.execute(patient_data)
    result["hypertension_screening"]=hypertension_screening.execute(patient_data)
    result["diabetes_screening"]=diabetes_screening.execute(patient_data)
    result["high_body_mass_index"]=high_body_mass_index.execute(patient_data)

    result["pregnancy_healthy_weight_gain"]=pregnancy_healthy_weight_gain.get_pregnancy_healthy_weight_gain_recommendation(pregnant=patient_data["pregnant"])
    result["prevent_obesity_morbidity_mortality"]=prevent_obesity_morbidity_mortality.get_obesity_recommendation(age=patient_data["age"],bmi=patient_data["bmi"])
 
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
    
# export FLASK_APP=demo.app:app 
# flask run 
 