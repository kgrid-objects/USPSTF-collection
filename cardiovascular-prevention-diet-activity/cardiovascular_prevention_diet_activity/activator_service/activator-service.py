from ..knowledge import get_cardiovascular_disease_healthy_diet_activity_recommendation

def apply(input):
    return get_cardiovascular_disease_healthy_diet_activity_recommendation(input["age"], input["has_cardiovascular_risk_factors"])

