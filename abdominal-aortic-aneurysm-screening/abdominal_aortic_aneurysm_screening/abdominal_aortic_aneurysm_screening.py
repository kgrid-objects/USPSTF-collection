from ko.ko import Ko

from abdominal_aortic_aneurysm_screening.knowledge import get_abdominal_aortic_aneurysm_screening


class abdominal_aortic_aneurysm_screening(Ko):
    def __init__(self):
        super().__init__(__package__, [get_abdominal_aortic_aneurysm_screening])
        self.add_endpoint("/check-inclusion", tags=["abdominal_aortic_aneurysm_screening"])


ko_instance = abdominal_aortic_aneurysm_screening()
app = ko_instance.app

ko_instance.define_cli()
ko_instance.add_argument(
    "-a", "--age", type=float, required=True, help="Age of the person"
)
ko_instance.add_argument(
    "-g", "--gender", type=float, required=True, help="Gender of the individual (0 for women, 1 for men)."
)
ko_instance.add_argument(
    "--has_never_smoked", action='store_true', help="Indicate if the person has never smoked."
)
ko_instance.add_argument(
    "--has_ever_smoked", action='store_false', dest='has_never_smoked', help="Indicate if the person has ever smoked."
)


def cli():
    ko_instance.execute_cli()


def apply(input):
    return ko_instance.execute(input)
