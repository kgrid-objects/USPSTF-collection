from high_body_mass_index import high_body_mass_index
def test_knowledge():
    assert high_body_mass_index.get_high_body_mass_index_classification(age = 17,bmi_percentile = 97)["inclusion"] 
    assert not high_body_mass_index.get_high_body_mass_index_classification(age = 27,bmi_percentile = 97)["inclusion"] 
    assert not high_body_mass_index.get_high_body_mass_index_classification(age = 17,bmi_percentile = 94)["inclusion"] 
    assert high_body_mass_index.get_high_body_mass_index_classification(age = 18,bmi_percentile = 95)["inclusion"] 



