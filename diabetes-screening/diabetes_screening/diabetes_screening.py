from ko.ko import Ko

from diabetes_screening.knowledge import get_diabetes_screening_classification


class diabetes_screening(Ko):
    def __init__(self):
        super().__init__(__package__, [get_diabetes_screening_classification])
        self.add_endpoint("/check-inclusion", tags=["diabetes_screening"])


ko_instance = diabetes_screening()
app = ko_instance.app

ko_instance.define_cli()
ko_instance.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
ko_instance.add_argument(
    "-b", "--bmi", type=float, required=True, help="body mass index"
)


def cli():
    ko_instance.execute_cli()


def apply(input):
    return ko_instance.execute(input)
