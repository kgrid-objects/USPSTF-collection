from ko.ko import Ko

from high_body_mass_index.knowledge import get_high_body_mass_index_classification


class high_body_mass_index(Ko):
    def __init__(self):
        super().__init__(__package__, [get_high_body_mass_index_classification])
        self.add_endpoint("/check-inclusion", tags=["high_body_mass_index"])


ko_instance = high_body_mass_index()
app = ko_instance.app

ko_instance.define_cli()
ko_instance.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
ko_instance.add_argument(
    "-p", "--bmi_percentile", type=float, required=True, help="bmi percentile for age and sex"
)


def cli():
    ko_instance.execute_cli()


def apply(input):
    return ko_instance.execute(input)
