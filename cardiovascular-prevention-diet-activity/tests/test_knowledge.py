from cardiovascular_prevention_diet_activity import cardiovascular_prevention_diet_activity
def test_knowledge():
    assert not cardiovascular_prevention_diet_activity.get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 30, has_cardiovascular_risk_factors = False)["inclusion"] 
    assert not cardiovascular_prevention_diet_activity.get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 17, has_cardiovascular_risk_factors = True)["inclusion"] 
    assert cardiovascular_prevention_diet_activity.get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 40, has_cardiovascular_risk_factors = True)["inclusion"] 
    assert cardiovascular_prevention_diet_activity.get_cardiovascular_disease_healthy_diet_activity_recommendation(age = 40, has_cardiovascular_risk_factors = True)["grade"] == "B" 

    




