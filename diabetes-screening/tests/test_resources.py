
from diabetes_screening import diabetes_screening
from diabetes_screening.diabetes_screening import apply

def test_get_version():  
    ko_instance = diabetes_screening()
    version = ko_instance.get_version()
    assert version == "v1.1"
    
def test_metadata():
    ko_instance = diabetes_screening()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.1"


def test_execute():
    ko_instance = diabetes_screening()
    assert "Prediabetes and Type 2 Diabetes: Screening" == ko_instance.execute({
        "age":20,
        "bmi":30
        }, "get_diabetes_screening_classification")["title"]

def test_activator_function():
    assert "Prediabetes and Type 2 Diabetes: Screening" == apply({
        "age":20,
        "bmi":30
        })["title"]
    
