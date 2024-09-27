from diabetes_screening.knowledge import get_diabetes_screening_classification
def test_knowledge():
    assert not get_diabetes_screening_classification(age = 34,bmi = 31)["inclusion"] 
    assert get_diabetes_screening_classification(age = 35,bmi = 31)["inclusion"] 
    assert not get_diabetes_screening_classification(age = 35,bmi = 24)["inclusion"] 
    assert get_diabetes_screening_classification(age = 35,bmi = 25)["inclusion"] 
    assert get_diabetes_screening_classification(age = 70,bmi = 25)["inclusion"] 
    assert not get_diabetes_screening_classification(age = 71,bmi = 25)["inclusion"] 



