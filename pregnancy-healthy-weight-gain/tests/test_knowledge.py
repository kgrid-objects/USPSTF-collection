from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain
def test_knowledge():
    assert pregnancy_healthy_weight_gain.get_pregnancy_healthy_weight_gain_recommendation(pregnant= True)["inclusion"] 
    assert not pregnancy_healthy_weight_gain.get_pregnancy_healthy_weight_gain_recommendation(pregnant= False)["inclusion"] 




