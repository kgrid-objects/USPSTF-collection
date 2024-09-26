from high_body_mass_index.knowledge import get_high_body_mass_index_classification
def test_knowledge():
    assert get_high_body_mass_index_classification(age = 17,bmi_percentile = 97)["inclusion"] 
    assert not get_high_body_mass_index_classification(age = 27,bmi_percentile = 97)["inclusion"] 
    assert not get_high_body_mass_index_classification(age = 17,bmi_percentile = 94)["inclusion"] 
    assert get_high_body_mass_index_classification(age = 18,bmi_percentile = 95)["inclusion"] 



