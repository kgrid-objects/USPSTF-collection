from ..knowledge import get_diabetes_screening_classification

def apply(input):
    return get_diabetes_screening_classification(input["age"], input["bmi"])

