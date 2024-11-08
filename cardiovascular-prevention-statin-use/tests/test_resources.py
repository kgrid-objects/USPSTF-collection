
from cardiovascular_prevention_statin_use import cardiovascular_prevention_statin_use
from cardiovascular_prevention_statin_use.cardiovascular_prevention_statin_use import apply

def test_get_version():  
    ko_instance = cardiovascular_prevention_statin_use()
    version = ko_instance.get_version()
    assert version == "v1.0"
    
def test_metadata():
    ko_instance = cardiovascular_prevention_statin_use()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.0"


def test_execute():
    ko_instance = cardiovascular_prevention_statin_use()
    assert "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication" == ko_instance.execute({
        "age":20,
        "has_cardiovascular_risk_factors":True,
        "ten_year_CVD_risk":15
        }, "get_statin_use")["title"]

def test_activator_function():
    assert "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication" == apply({
        "age":20,
        "has_cardiovascular_risk_factors":False
        })["title"]
    
