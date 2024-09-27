from hypertension_screening.knowledge import get_hypertension_screening_classification
def test_knowledge():
    assert not get_hypertension_screening_classification(age = 17,hypertension= False)["inclusion"] 
    assert get_hypertension_screening_classification(age = 18,hypertension= False)["inclusion"] 
    assert not get_hypertension_screening_classification(age = 27,hypertension= True)["inclusion"] 
    assert get_hypertension_screening_classification(age = 30,hypertension= False)["inclusion"] 



