from ..knowledge import get_obesity_recommendation

def apply(input):
    return get_obesity_recommendation(input["age"], input["bmi"])

