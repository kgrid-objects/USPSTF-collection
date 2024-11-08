
from cardiovascular_prevention_diet_activity import cardiovascular_prevention_diet_activity
from cardiovascular_prevention_diet_activity.cardiovascular_prevention_diet_activity import apply

def test_get_version():  
    ko_instance = cardiovascular_prevention_diet_activity()
    version = ko_instance.get_version()
    assert version == "v1.0"
    
def test_metadata():
    ko_instance = cardiovascular_prevention_diet_activity()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.0"


def test_execute():
    ko_instance = cardiovascular_prevention_diet_activity()
    assert "Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions" == ko_instance.execute({
        "age":20,
        "has_cardiovascular_risk_factors":True
        }, "get_cardiovascular_disease_healthy_diet_activity_recommendation")["title"]

def test_activator_function():
    assert "Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions" == apply({
        "age":20,
        "has_cardiovascular_risk_factors":False
        })["title"]
    
