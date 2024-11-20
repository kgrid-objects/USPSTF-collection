
from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain

def test_get_version():  
    version = pregnancy_healthy_weight_gain.get_version()
    assert version == "v1.3"
    
def test_metadata():
    version = pregnancy_healthy_weight_gain.get_metadata().get('version', 'Unknown version')
    assert version == "v1.3"

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
    
