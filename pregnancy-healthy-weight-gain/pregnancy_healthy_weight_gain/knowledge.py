def get_pregnancy_healthy_weight_gain_recommendation(pregnant):
    """
    Parameters:
    - pregnant (bool): Indicated if the person is pregnant.
    """
    
    if not pregnant:
        return {
            "inclusion": False
            }
    else:
        return {
            "inclusion": True,
            "recommendation": "The USPSTF recommends that clinicians offer pregnant persons effective behavioral counseling interventions aimed at promoting healthy weight gain and preventing excess gestational weight gain in pregnancy.",
            "grade": "B",
            "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/healthy-weight-and-weight-gain-during-pregnancy-behavioral-counseling-interventions"
            }