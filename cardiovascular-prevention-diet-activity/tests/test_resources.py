
from cardiovascular_prevention_diet_activity import cardiovascular_prevention_diet_activity
from cardiovascular_prevention_diet_activity import apply

def test_get_version():  
    version = cardiovascular_prevention_diet_activity.get_version()
    assert version == "v1.5"
    
def test_metadata():
    version = cardiovascular_prevention_diet_activity.get_metadata().get('version', 'Unknown version')
    assert version == "v1.5"


def test_execute():
    assert "Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions" == cardiovascular_prevention_diet_activity.execute({
        "age":20,
        "has_cardiovascular_risk_factors":True
        }, "get_cardiovascular_disease_healthy_diet_activity_recommendation")["title"]

def test_activator_function():
    assert "Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions" == apply({
        "age":20,
        "has_cardiovascular_risk_factors":False
        })["title"]

def test_direct_call():
    assert cardiovascular_prevention_diet_activity.get_cardiovascular_disease_healthy_diet_activity_recommendation(
         35 , False
    ) == {
            "inclusion": False,
            "title": "Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions"   
            }
    
