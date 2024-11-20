from kgrid_sdk import Ko_API
from kgrid_sdk import Ko_CLI



class Cardiovascular_prevention_diet_activity(Ko_API,Ko_CLI):
    def __init__(self):
        super().__init__(__package__, [self.get_cardiovascular_disease_healthy_diet_activity_recommendation])
        self.add_endpoint("/check-inclusion", tags=["cardiovascular_prevention_diet_activity"])

    @staticmethod
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

cardiovascular_prevention_diet_activity = Cardiovascular_prevention_diet_activity()
app = cardiovascular_prevention_diet_activity.app

cardiovascular_prevention_diet_activity.define_cli()
cardiovascular_prevention_diet_activity.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
cardiovascular_prevention_diet_activity.add_argument(
    "-c", "--has_cardiovascular_risk_factors", action='store_true', help="Indicate if the person has cardiovascular risk factors (e.g., dyslipidemia, diabetes, hypertension, or smoking)."
)
cardiovascular_prevention_diet_activity.add_argument(
   "--no_cardiovascular_risk_factors", action='store_false', dest='has_cardiovascular_risk_factors', help="Indicate if the person does NOT have cardiovascular risk factors."
)


def cli():
    cardiovascular_prevention_diet_activity.execute_cli()


def apply(input):
    return cardiovascular_prevention_diet_activity.execute(input)
