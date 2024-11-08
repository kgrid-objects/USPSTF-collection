from ko.ko import Ko

from cardiovascular_prevention_diet_activity.knowledge import get_cardiovascular_disease_healthy_diet_activity_recommendation


class cardiovascular_prevention_diet_activity(Ko):
    def __init__(self):
        super().__init__(__package__, [get_cardiovascular_disease_healthy_diet_activity_recommendation])
        self.add_endpoint("/check-inclusion", tags=["cardiovascular_prevention_diet_activity"])


ko_instance = cardiovascular_prevention_diet_activity()
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


def cli():
    ko_instance.execute_cli()


def apply(input):
    return ko_instance.execute(input)
