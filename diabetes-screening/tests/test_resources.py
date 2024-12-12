
from diabetes_screening import diabetes_screening
from diabetes_screening import apply
version = "v1.8"
def test_get_version():  
    assert version == diabetes_screening.get_version()
    
def test_metadata():
    assert version == diabetes_screening.get_metadata().get('dc:version', 'Unknown version')


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
