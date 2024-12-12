from cardiovascular_prevention_statin_use import cardiovascular_prevention_statin_use
def test_knowledge():
    assert not cardiovascular_prevention_statin_use.get_statin_use(age = 30, has_cardiovascular_risk_factors = True, ten_year_CVD_risk = 15)["inclusion"] 
    assert cardiovascular_prevention_statin_use.get_statin_use(age = 40, has_cardiovascular_risk_factors = True, ten_year_CVD_risk = 15)["inclusion"] 
    assert cardiovascular_prevention_statin_use.get_statin_use(age = 40, has_cardiovascular_risk_factors = True, ten_year_CVD_risk = 15)["grade"] == "B" 
    assert cardiovascular_prevention_statin_use.get_statin_use(age = 40, has_cardiovascular_risk_factors = True, ten_year_CVD_risk = 7.5)["grade"] == "C"    
    assert not cardiovascular_prevention_statin_use.get_statin_use(age = 30, has_cardiovascular_risk_factors = True, ten_year_CVD_risk = 7.5)["inclusion"] 
    assert cardiovascular_prevention_statin_use.get_statin_use(age = 76, has_cardiovascular_risk_factors = False, ten_year_CVD_risk = 5)["inclusion"] 
    assert cardiovascular_prevention_statin_use.get_statin_use(age = 76, has_cardiovascular_risk_factors = False, ten_year_CVD_risk = 5)["grade"] == "I" 
    assert not cardiovascular_prevention_statin_use.get_statin_use(age = 50, has_cardiovascular_risk_factors = True, ten_year_CVD_risk = 5)["inclusion"] 
    




