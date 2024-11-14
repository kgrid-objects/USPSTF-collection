from flask import Flask, render_template, jsonify, request
from abdominal_aortic_aneurysm_screening import abdominal_aortic_aneurysm_screening
from cardiovascular_prevention_diet_activity import cardiovascular_prevention_diet_activity
from cardiovascular_prevention_statin_use import cardiovascular_prevention_statin_use
from hypertension_screening import hypertension_screening
from diabetes_screening import diabetes_screening
from high_body_mass_index import high_body_mass_index
from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain
from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality
from kgrid.collection import Collection
app = Flask(__name__)



@app.route("/")
def index():
    # Render the HTML page with patient data
    return render_template("index.html")

@app.route("/get_result", methods=["POST"])
def get_result():
    patient_data = request.get_json()
    collection = Collection("USPSTF_Collection_1")
    collection.add_knowledge_object( abdominal_aortic_aneurysm_screening )
    collection.add_knowledge_object( cardiovascular_prevention_diet_activity )
    collection.add_knowledge_object( cardiovascular_prevention_statin_use )
    collection.add_knowledge_object( hypertension_screening )
    collection.add_knowledge_object( diabetes_screening )
    collection.add_knowledge_object( high_body_mass_index )
    

    result = collection.calculate_for_all(patient_data)
    
    result["pregnancy_healthy_weight_gain"]=pregnancy_healthy_weight_gain.get_pregnancy_healthy_weight_gain_recommendation(pregnant=patient_data["pregnant"])
    result["prevent_obesity_morbidity_mortality"]=prevent_obesity_morbidity_mortality.get_obesity_recommendation(age=patient_data["age"],bmi=patient_data["bmi"])
 
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
    
# export FLASK_APP=sdk_demo.app:app 
# flask run 
 