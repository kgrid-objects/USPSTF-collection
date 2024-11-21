from kgrid_sdk import Ko_API
from kgrid_sdk import Ko_CLI



class High_body_mass_index(Ko_API,Ko_CLI):
    def __init__(self):
        super().__init__( [self.get_high_body_mass_index_classification])
        self.add_endpoint("/check-inclusion", tags=["high_body_mass_index"])
        
    @staticmethod
    def get_high_body_mass_index_classification(age:int, bmi_percentile:float):
        """
        Parameters:
        - age (int): Age of the person.
        - bmi_percentile (float): bmi percentile for age and sex.
        """
        
        if age < 6 or age > 18 or bmi_percentile < 95:
            return {
                "inclusion": False,
                "title": "High Body Mass Index in Children and Adolescents: Interventions"
                }
        else:
            return {
                "inclusion": True,
                "title": "High Body Mass Index in Children and Adolescents: Interventions",
                "recommendation": "The USPSTF recommends that clinicians provide or refer children and adolescents 6 years or older with a high body mass index (BMI) (≥95th percentile for age and sex) to comprehensive, intensive behavioral interventions.",
                "grade": "B",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obesity-in-children-and-adolescents-screening"
                }


high_body_mass_index = High_body_mass_index()
app = high_body_mass_index.app

high_body_mass_index.define_cli()
high_body_mass_index.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
high_body_mass_index.add_argument(
    "-p", "--bmi_percentile", type=float, required=True, help="bmi percentile for age and sex"
)


def cli():
    high_body_mass_index.execute_cli()


def apply(input):
    return high_body_mass_index.execute(input)
