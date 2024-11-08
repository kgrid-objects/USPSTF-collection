from ko.ko import Ko

from cardiovascular_prevention_statin_use.knowledge import get_statin_use


class cardiovascular_prevention_statin_use(Ko):
    def __init__(self):
        super().__init__(__package__, [get_statin_use])
        self.add_endpoint("/check-inclusion", tags=["cardiovascular_prevention_statin_use"])


ko_instance = cardiovascular_prevention_statin_use()
app = ko_instance.app

ko_instance.define_cli()
ko_instance.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
ko_instance.add_argument(
    "-c", "--has_cardiovascular_risk_factors", action='store_true', help="Indicate if the person has cardiovascular risk factors (e.g., dyslipidemia, diabetes, hypertension, or smoking)."
)
ko_instance.add_argument(
   "--no_cardiovascular_risk_factors", action='store_false', dest='has_cardiovascular_risk_factors', help="Indicate if the person does NOT have cardiovascular risk factors."
)
ko_instance.add_argument(
   "-t", "--ten_year_CVD_risk", type=float, required=True, help="The probability that an individual will have a cardiovascular event (such as a heart attack or stroke) within the next 10 years (0 to 100)."
)

def cli():
    ko_instance.execute_cli()


def apply(input):
    return ko_instance.execute(input)
