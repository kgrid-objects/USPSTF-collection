from kgrid_sdk import Ko_API
from kgrid_sdk import Ko_CLI



class Diabetes_screening(Ko_API,Ko_CLI):
    def __init__(self):
        super().__init__( [self.get_diabetes_screening_classification])
        self.add_endpoint("/check-inclusion", tags=["diabetes_screening"])
        
    @staticmethod
    def get_diabetes_screening_classification(age, bmi):
        """
        Parameters:
        - age (int): Age of the person.
        - bmi (float): body mass index.
        """
        
        if age >= 35 and age <=70 and bmi >= 25:
            return {
                "inclusion": True,
                "title": "Prediabetes and Type 2 Diabetes: Screening",
                "recommendation": "The USPSTF recommends screening for prediabetes and type 2 diabetes in adults aged 35 to 70 years who have overweight or obesity. Clinicians should offer or refer patients with prediabetes to effective preventive interventions.",
                "grade": "B",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes"
                }
        else:
            return {
                "inclusion": False,
                "title": "Prediabetes and Type 2 Diabetes: Screening"
                }
            


diabetes_screening = Diabetes_screening()
app = diabetes_screening.app

diabetes_screening.define_cli()
diabetes_screening.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
diabetes_screening.add_argument(
    "-b", "--bmi", type=float, required=True, help="body mass index"
)


def cli():
    diabetes_screening.execute_cli()


def apply(input):
    return diabetes_screening.execute(input)
