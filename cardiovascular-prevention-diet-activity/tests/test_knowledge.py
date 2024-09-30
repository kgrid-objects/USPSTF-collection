from cardiovascular_prevention_diet_activity.knowledge import get_cardiovascular_disease_healthy_diet_activity_recommendation
def test_knowledge():
    assert not get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 30, has_cardiovascular_risk_factors = False)["inclusion"] 
    assert not get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 17, has_cardiovascular_risk_factors = True)["inclusion"] 
    assert get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 40, has_cardiovascular_risk_factors = True)["inclusion"] 
    assert get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 40, has_cardiovascular_risk_factors = True)["grade"] == "B" 

    




