from ..knowledge import get_hypertension_screening_classification

def apply(input):
    return get_hypertension_screening_classification(input["age"], input["hypertension"])

