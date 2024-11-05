
from hypertension_screening import hypertension_screening

def test_get_version():  
    ko_instance = hypertension_screening()
    version = ko_instance.get_version()
    assert version == "v1.0"
    
def test_metadata():
    ko_instance = hypertension_screening()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.0"


    