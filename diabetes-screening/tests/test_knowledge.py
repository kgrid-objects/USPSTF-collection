from diabetes_screening import diabetes_screening
def test_knowledge():
    assert not diabetes_screening.get_diabetes_screening_classification(age = 34,bmi = 31)["inclusion"] 
    assert diabetes_screening.get_diabetes_screening_classification(age = 35,bmi = 31)["inclusion"] 
    assert not diabetes_screening.get_diabetes_screening_classification(age = 35,bmi = 24)["inclusion"] 
    assert diabetes_screening.get_diabetes_screening_classification(age = 35,bmi = 25)["inclusion"] 
    assert diabetes_screening.get_diabetes_screening_classification(age = 70,bmi = 25)["inclusion"] 
    assert not diabetes_screening.get_diabetes_screening_classification(age = 71,bmi = 25)["inclusion"] 



