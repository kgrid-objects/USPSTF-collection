from ko.ko import Ko
from hypertension_screening.knowledge import get_hypertension_screening_classification
class hypertension_screening(Ko):
    
    def __init__(self):
        super().__init__( __package__, [get_hypertension_screening_classification])
        self.add_endpoint("/check-inclusion", tags=["hypertension_screening"])
        
ko_instance = hypertension_screening()
app = ko_instance.app     

ko_instance.define_cli()
ko_instance.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
ko_instance.add_argument("-t", "--hypertension", action="store_true", help="Indicate if the person is diagnosed with hypertension.")
ko_instance.add_argument("--no-hypertension", action="store_false", dest="hypertension", help="Indicate if the person is NOT diagnosed with hypertension.")

def cli():
    ko_instance.execute_cli()   

def apply(input):
    return ko_instance.execute(input)
    #return ko_instance.execute1(age=20,hypertension=False)