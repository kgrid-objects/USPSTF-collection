from pregnancy_healthy_weight_gain.knowledge import get_pregnancy_healthy_weight_gain_recommendation
def test_knowledge():
    assert get_pregnancy_healthy_weight_gain_recommendation(pregnant= True)["inclusion"] 
    assert not get_pregnancy_healthy_weight_gain_recommendation(pregnant= False)["inclusion"] 




