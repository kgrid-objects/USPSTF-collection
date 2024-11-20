
from cardiovascular_prevention_statin_use import cardiovascular_prevention_statin_use
from cardiovascular_prevention_statin_use import apply

def test_get_version():  
    version = cardiovascular_prevention_statin_use.get_version()
    assert version == "v1.3"
    
def test_metadata():
    version = cardiovascular_prevention_statin_use.get_metadata().get('version', 'Unknown version')
    assert version == "v1.3"


def test_execute():
    assert "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication" == cardiovascular_prevention_statin_use.execute({
        "age":20,
        "has_cardiovascular_risk_factors":True,
        "ten_year_CVD_risk":15
        }, "get_statin_use")["title"]

def test_activator_function():
    assert "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication" == apply({
        "age":20,
        "has_cardiovascular_risk_factors":False,
        "ten_year_CVD_risk":15
        })["title"]
    
def test_direct_call():
    assert cardiovascular_prevention_statin_use.get_statin_use(
         35 , False, None
    ) == {
            "inclusion": False,
            "title": "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication"
            }
