from ko.ko import Ko

from prevent_obesity_morbidity_mortality.knowledge import get_obesity_recommendation


class prevent_obesity_morbidity_mortality(Ko):
    def __init__(self):
        super().__init__(__package__, [get_obesity_recommendation])
        self.add_endpoint("/check-inclusion", tags=["prevent_obesity_morbidity_mortality"])


ko_instance = prevent_obesity_morbidity_mortality()
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
