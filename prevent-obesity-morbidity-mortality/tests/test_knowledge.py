from prevent_obesity_morbidity_mortality.knowledge import get_obesity_recommendation
def test_knowledge():
    assert not get_obesity_recommendation(age = 17,bmi = 31)["inclusion"] 
    assert get_obesity_recommendation(age = 18,bmi = 31)["inclusion"] 
    assert not get_obesity_recommendation(age = 18,bmi = 29)["inclusion"] 
    assert get_obesity_recommendation(age = 18,bmi = 30)["inclusion"] 




