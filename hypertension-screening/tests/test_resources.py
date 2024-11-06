
from hypertension_screening import hypertension_screening
from hypertension_screening.activator_service import activator_service

def test_get_version():  
    ko_instance = hypertension_screening()
    version = ko_instance.get_version()
    assert version == "v1.0"
    
def test_metadata():
    ko_instance = hypertension_screening()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.0"


def test_execute():
    ko_instance = hypertension_screening()
    assert "Hypertension in Adults: Screening" == ko_instance.execute({
        "age":20,
        "hypertension":False
        }, "get_hypertension_screening_classification")["title"]

def test_activator_function():
    assert "Hypertension in Adults: Screening" == activator_service.apply({
        "age":20,
        "hypertension":False
        })["title"]
    