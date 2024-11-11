
from high_body_mass_index import high_body_mass_index
from high_body_mass_index.high_body_mass_index import apply

def test_get_version():  
    ko_instance = high_body_mass_index()
    version = ko_instance.get_version()
    assert version == "v1.1"
    
def test_metadata():
    ko_instance = high_body_mass_index()
    version = ko_instance.get_metadata().get('version', 'Unknown version')
    assert version == "v1.1"


def test_execute():
    ko_instance = high_body_mass_index()
    assert "High Body Mass Index in Children and Adolescents: Interventions" == ko_instance.execute({
        "age":17,
        "bmi_percentile":95
        }, "get_high_body_mass_index_classification")["title"]

def test_activator_function():
    assert "High Body Mass Index in Children and Adolescents: Interventions" == apply({
        "age":17,
        "bmi_percentile":95
        })["title"]
    
