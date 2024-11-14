from kgrid import Ko_API
from kgrid import Ko_CLI

      

class Hypertension_screening(Ko_API, Ko_CLI):
    def __init__(self):
        super().__init__(__package__, [self.get_hypertension_screening_classification])
        self.add_endpoint("/check-inclusion", tags=["hypertension_screening"])

 
    @staticmethod
    def get_hypertension_screening_classification(age:int, hypertension:bool):
        """
        Parameters:
        - age (int): Age of the person.
        - hypertension (bool): Indicated whether the person diagnosed for hypertension or not.
        """

        if age >= 18 and not hypertension:
            return {
                "inclusion": True,
                "title": "Hypertension in Adults: Screening",
                "recommendation": "The USPSTF recommends screening for hypertension in adults 18 years or older with office blood pressure measurement (OBPM). The USPSTF recommends obtaining blood pressure measurements outside of the clinical setting for diagnostic confirmation before starting treatment.",
                "grade": "A",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening",
            }
        else:
            return {"inclusion": False, "title": "Hypertension in Adults: Screening"}
        


hypertension_screening = Hypertension_screening()
app = hypertension_screening.app

hypertension_screening.define_cli()
hypertension_screening.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
hypertension_screening.add_argument(
    "-t",
    "--hypertension",
    action="store_true",
    help="Indicate if the person is diagnosed with hypertension.",
)
hypertension_screening.add_argument(
    "--no-hypertension",
    action="store_false",
    dest="hypertension",
    help="Indicate if the person is NOT diagnosed with hypertension.",
)


def cli():
    hypertension_screening.execute_cli()


def apply(input):
    return hypertension_screening.execute(input)
