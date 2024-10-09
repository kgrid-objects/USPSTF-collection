def get_cardiovascular_disease_healthy_diet_activity_recommendation(age, has_cardiovascular_risk_factors):
    """
    Parameters:
    - age (int): Age of the person.
    - has_cardiovascular_risk_factors (bool): Whether this person has CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) or not.
    """
    
    if age >= 18 and has_cardiovascular_risk_factors:
        return {
            "inclusion": True,
            "title": "Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions",
            "recommendation": "The USPSTF recommends offering or referring adults with cardiovascular disease risk factors to behavioral counseling interventions to promote a healthy diet and physical activity.",
            "grade": "B",
            "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/healthy-diet-and-physical-activity-counseling-adults-with-high-risk-of-cvd"
            }
    
    return {
        "inclusion": False,
        "title": "Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions"   
        }
        