
from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain
version = "v1.6"
def test_get_version():  
    assert version == pregnancy_healthy_weight_gain.get_version()
    
def test_metadata():
    assert version == pregnancy_healthy_weight_gain.get_metadata().get('version', 'Unknown version')

def test_execute():
    assert "Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions" == pregnancy_healthy_weight_gain.execute({
        "pregnant":True
        }, "get_pregnancy_healthy_weight_gain_recommendation")["title"]

def test_direct_call():
    assert pregnancy_healthy_weight_gain.get_pregnancy_healthy_weight_gain_recommendation(
         False
    ) == {
                "inclusion": False,
                "title": "Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions"
                }
    
