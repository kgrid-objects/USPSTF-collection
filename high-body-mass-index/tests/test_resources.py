
from high_body_mass_index import high_body_mass_index
from high_body_mass_index import apply

def test_get_version():  
    version = high_body_mass_index.get_version()
    assert version == "v1.2"
    
def test_metadata():
    version = high_body_mass_index.get_metadata().get('version', 'Unknown version')
    assert version == "v1.2"


def test_execute():
    assert "High Body Mass Index in Children and Adolescents: Interventions" == high_body_mass_index.execute({
        "age":17,
        "bmi_percentile":95
        }, "get_high_body_mass_index_classification")["title"]

def test_activator_function():
    assert "High Body Mass Index in Children and Adolescents: Interventions" == apply({
        "age":17,
        "bmi_percentile":95
        })["title"]
    
def test_direct_call():
    assert high_body_mass_index.get_high_body_mass_index_classification(
         35 , 80
    ) == {
                "inclusion": False,
                "title": "High Body Mass Index in Children and Adolescents: Interventions"
                }
