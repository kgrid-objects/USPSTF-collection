
from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality
from prevent_obesity_morbidity_mortality.prevent_obesity_morbidity_mortality import apply

def test_get_version():  
    ko_instance = prevent_obesity_morbidity_mortality()
    version = ko_instance.get_version()
    assert version == "v1.1"
    
def test_metadata():
    ko_instance = prevent_obesity_morbidity_mortality()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.1"


def test_execute():
    ko_instance = prevent_obesity_morbidity_mortality()
    assert "Weight Loss to Prevent Obesity-Related Morbidity and Mortality in Adults: Behavioral Interventions" == ko_instance.execute({
        "age":20,
        "bmi":30
        }, "get_obesity_recommendation")["title"]

def test_activator_function():
    assert "Weight Loss to Prevent Obesity-Related Morbidity and Mortality in Adults: Behavioral Interventions" == apply({
        "age":20,
        "bmi":30
        })["title"]
    
