
from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain
from pregnancy_healthy_weight_gain.pregnancy_healthy_weight_gain import apply

def test_get_version():  
    ko_instance = pregnancy_healthy_weight_gain()
    version = ko_instance.get_version()
    assert version == "v1.1"
    
def test_metadata():
    ko_instance = pregnancy_healthy_weight_gain()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.1"


def test_execute():
    ko_instance = pregnancy_healthy_weight_gain()
    assert "Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions" == ko_instance.execute({
        "pregnant":True
        }, "get_pregnancy_healthy_weight_gain_recommendation")["title"]

def test_activator_function():
    assert "Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions" == apply({
        "pregnant":True
        })["title"]
    
