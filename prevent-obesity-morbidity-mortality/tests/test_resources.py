
from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality

def test_get_version():  
    version = prevent_obesity_morbidity_mortality.get_version()
    assert version == "v1.5"
    
def test_metadata():
    version = prevent_obesity_morbidity_mortality.get_metadata().get('version', 'Unknown version')
    assert version == "v1.5"


def test_direct_call():
    assert prevent_obesity_morbidity_mortality.get_obesity_recommendation(
         35 , 18
    ) == {
                "inclusion": False,
                "title": "Weight Loss to Prevent Obesity-Related Morbidity and Mortality in Adults: Behavioral Interventions"
                }