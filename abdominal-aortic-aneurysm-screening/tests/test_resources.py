
from abdominal_aortic_aneurysm_screening import abdominal_aortic_aneurysm_screening
from abdominal_aortic_aneurysm_screening.abdominal_aortic_aneurysm_screening import Abdominal_aortic_aneurysm_screening

from abdominal_aortic_aneurysm_screening import apply
version = "v1.5"
def test_get_version():  
    
    assert version == abdominal_aortic_aneurysm_screening.get_version()
    assert version == Abdominal_aortic_aneurysm_screening.get_version()  
    
def test_metadata():
    assert version == abdominal_aortic_aneurysm_screening.get_metadata().get('version', 'Unknown version')

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
    
    
