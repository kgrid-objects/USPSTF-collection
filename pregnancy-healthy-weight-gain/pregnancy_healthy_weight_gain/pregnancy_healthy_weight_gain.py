from kgrid_sdk import Ko_Execution


class Pregnancy_healthy_weight_gain(Ko_Execution):
    def __init__(self):
        super().__init__(__package__, [self.get_pregnancy_healthy_weight_gain_recommendation])

    @staticmethod
    def get_pregnancy_healthy_weight_gain_recommendation(pregnant):
        """
        Parameters:
        - pregnant (bool): Indicated if the person is pregnant.
        """
        
        if not pregnant:
            return {
                "inclusion": False,
                "title": "Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions"
                }
        else:
            return {
                "inclusion": True,
                "title": "Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions",
                "recommendation": "The USPSTF recommends that clinicians offer pregnant persons effective behavioral counseling interventions aimed at promoting healthy weight gain and preventing excess gestational weight gain in pregnancy.",
                "grade": "B",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/healthy-weight-and-weight-gain-during-pregnancy-behavioral-counseling-interventions"
                }
        
pregnancy_healthy_weight_gain = Pregnancy_healthy_weight_gain()

