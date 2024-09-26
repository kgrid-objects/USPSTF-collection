from ..knowledge import get_high_body_mass_index_classification

def apply(input):
    return get_high_body_mass_index_classification(input["age"], input["bmi_percentile"])

