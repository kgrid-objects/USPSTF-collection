from ko.ko import Ko

from pregnancy_healthy_weight_gain.knowledge import get_pregnancy_healthy_weight_gain_recommendation


class pregnancy_healthy_weight_gain(Ko):
    def __init__(self):
        super().__init__(__package__, [get_pregnancy_healthy_weight_gain_recommendation])
        self.add_endpoint("/check-inclusion", tags=["pregnancy_healthy_weight_gain"])


ko_instance = pregnancy_healthy_weight_gain()
app = ko_instance.app

ko_instance.define_cli()
ko_instance.add_argument(
    "-p", "--pregnant", action='store_true', help="Indicate if the person is pregnant."
)
ko_instance.add_argument(
    "--not-pregnant", action='store_false', dest='pregnant', help="Indicate if the person is NOT pregnant."
)


def cli():
    ko_instance.execute_cli()


def apply(input):
    return ko_instance.execute(input)
