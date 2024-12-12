
from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality
version = "v1.8"
def test_get_version():  
    assert version == prevent_obesity_morbidity_mortality.get_version()
    
def test_metadata():
    assert version == prevent_obesity_morbidity_mortality.get_metadata().get('version', 'Unknown version')


def test_direct_call():
    assert prevent_obesity_morbidity_mortality.get_obesity_recommendation(
         35 , 18
    ) == {
                "inclusion": False,
                "title": "Weight Loss to Prevent Obesity-Related Morbidity and Mortality in Adults: Behavioral Interventions"
                }