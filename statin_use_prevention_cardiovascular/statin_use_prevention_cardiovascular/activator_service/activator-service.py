from ..knowledge import get_statin_use

def apply(input):
    return get_statin_use(input["age"], input["has_cardiovascular_risk_factors"], input["ten_year_CVD_risk"])

