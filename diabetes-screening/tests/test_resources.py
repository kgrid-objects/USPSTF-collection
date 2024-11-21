
from diabetes_screening import diabetes_screening
from diabetes_screening import apply

def test_get_version():  
    version = diabetes_screening.get_version()
    assert version == "v1.5"
    
def test_metadata():
    version = diabetes_screening.get_metadata().get('version', 'Unknown version')
    assert version == "v1.5"


def test_execute():
    assert "Prediabetes and Type 2 Diabetes: Screening" == diabetes_screening.execute({
        "age":20,
        "bmi":30
        }, "get_diabetes_screening_classification")["title"]

def test_activator_function():
    assert "Prediabetes and Type 2 Diabetes: Screening" == apply({
        "age":20,
        "bmi":30
        })["title"]
    
def test_direct_call():
    assert diabetes_screening.get_diabetes_screening_classification(
         20 , 30
    ) == {
                "inclusion": False,
                "title": "Prediabetes and Type 2 Diabetes: Screening"
                }
