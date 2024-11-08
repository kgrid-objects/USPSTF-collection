
from abdominal_aortic_aneurysm_screening import abdominal_aortic_aneurysm_screening
from abdominal_aortic_aneurysm_screening.abdominal_aortic_aneurysm_screening import apply

def test_get_version():  
    ko_instance = abdominal_aortic_aneurysm_screening()
    version = ko_instance.get_version()
    assert version == "v1.0"
    
def test_metadata():
    ko_instance = abdominal_aortic_aneurysm_screening()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.0"


def test_execute():
    ko_instance = abdominal_aortic_aneurysm_screening()
    assert "Abdominal Aortic Aneurysm: Screening" == ko_instance.execute({
        "age":20,
        "gender": 0,
        "has_never_smoked":False
        }, "get_abdominal_aortic_aneurysm_screening")["title"]

def test_activator_function():
    assert "Abdominal Aortic Aneurysm: Screening" == apply({
        "age":20,
        "gender": 0,
        "has_never_smoked":False
        })["title"]
    
