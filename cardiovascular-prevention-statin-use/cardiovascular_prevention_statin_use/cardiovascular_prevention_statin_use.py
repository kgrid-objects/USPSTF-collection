from kgrid_sdk import Ko_API
from kgrid_sdk import Ko_CLI



class Cardiovascular_prevention_statin_use(Ko_API,Ko_CLI):
    def __init__(self):
        super().__init__( [self.get_statin_use])
        self.add_endpoint("/check-inclusion", tags=["cardiovascular_prevention_statin_use"])

    @staticmethod
    def get_statin_use(age, has_cardiovascular_risk_factors, ten_year_CVD_risk):
        """
        Parameters:
        - age (int): Age of the person.
        - has_cardiovascular_risk_factors (bool): Whether this person has CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) or not.
        - ten_year_CVD_risk (float): The probability that an individual will have a cardiovascular event (such as a heart attack or stroke) within the next 10 years (0 to 100).
        """
        
        if age >= 40 and age <= 75 and has_cardiovascular_risk_factors:
            if ten_year_CVD_risk >= 10:
                return {
                    "inclusion": True,
                    "title": "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication",
                    "recommendation": "The USPSTF recommends that clinicians prescribe a statin for the primary prevention of CVD for adults aged 40 to 75 years who have 1 or more CVD risk factors (i.e. dyslipidemia, diabetes, hypertension, or smoking) and an estimated 10-year risk of a cardiovascular event of 10% or greater.",
                    "grade": "B",
                    "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication#fullrecommendationstart"
                    }
            elif ten_year_CVD_risk >= 7.5:
                return {
                    "inclusion": True,
                    "title": "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication",
                    "recommendation": "The USPSTF recommends that clinicians selectively offer a statin for the primary prevention of CVD for adults aged 40 to 75 years who have 1 or more CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) and an estimated 10-year risk of a cardiovascular event of 7.5% to less than 10%. The likelihood of benefit is smaller in this group than in persons with a 10-year risk of 10% or greater.",
                    "grade": "C",
                    "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication#fullrecommendationstart"
                    }
        elif age >= 76:
            return {
                    "inclusion": True,
                    "title": "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication",
                    "recommendation": "	The USPSTF concludes that the current evidence is insufficient to assess the balance of benefits and harms of initiating a statin for the primary prevention of CVD events and mortality in adults 76 years or older.",
                    "grade": "I",
                    "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication#fullrecommendationstart"
                    }   
        return {
            "inclusion": False,
            "title": "Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication"
            }
            

cardiovascular_prevention_statin_use = Cardiovascular_prevention_statin_use()
app = cardiovascular_prevention_statin_use.app

cardiovascular_prevention_statin_use.define_cli()
cardiovascular_prevention_statin_use.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
cardiovascular_prevention_statin_use.add_argument(
    "-c", "--has_cardiovascular_risk_factors", action='store_true', help="Indicate if the person has cardiovascular risk factors (e.g., dyslipidemia, diabetes, hypertension, or smoking)."
)
cardiovascular_prevention_statin_use.add_argument(
   "--no_cardiovascular_risk_factors", action='store_false', dest='has_cardiovascular_risk_factors', help="Indicate if the person does NOT have cardiovascular risk factors."
)
cardiovascular_prevention_statin_use.add_argument(
   "-t", "--ten_year_CVD_risk", type=float, required=True, help="The probability that an individual will have a cardiovascular event (such as a heart attack or stroke) within the next 10 years (0 to 100)."
)

def cli():
    cardiovascular_prevention_statin_use.execute_cli()


def apply(input):
    return cardiovascular_prevention_statin_use.execute(input)
