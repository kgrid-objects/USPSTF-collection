
from abdominal_aortic_aneurysm_screening import abdominal_aortic_aneurysm_screening
from abdominal_aortic_aneurysm_screening import apply

def test_get_version():  
    version = abdominal_aortic_aneurysm_screening.get_version()
    assert version == "v1.1"
    
def test_metadata():
    version = abdominal_aortic_aneurysm_screening.get_metadata().get('version', 'Unknown version')
    assert version == "v1.1"


def test_execute():
    assert "Abdominal Aortic Aneurysm: Screening" == abdominal_aortic_aneurysm_screening.execute({
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
    
