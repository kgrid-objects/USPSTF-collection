from hypertension_screening import hypertension_screening
def test_knowledge():
    assert not hypertension_screening.get_hypertension_screening_classification(age = 17,hypertension= False)["inclusion"] 
    assert hypertension_screening.get_hypertension_screening_classification(age = 18,hypertension= False)["inclusion"] 
    assert not hypertension_screening.get_hypertension_screening_classification(age = 27,hypertension= True)["inclusion"] 
    assert hypertension_screening.get_hypertension_screening_classification(age = 30,hypertension= False)["inclusion"] 



