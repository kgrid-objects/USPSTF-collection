from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality
def test_knowledge():
    assert not prevent_obesity_morbidity_mortality.get_obesity_recommendation(age = 17,bmi = 31)["inclusion"] 
    assert prevent_obesity_morbidity_mortality.get_obesity_recommendation(age = 18,bmi = 31)["inclusion"] 
    assert not prevent_obesity_morbidity_mortality.get_obesity_recommendation(age = 18,bmi = 29)["inclusion"] 
    assert prevent_obesity_morbidity_mortality.get_obesity_recommendation(age = 18,bmi = 30)["inclusion"] 




