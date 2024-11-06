from ko.ko import Ko
from hypertension_screening.knowledge import get_hypertension_screening_classification
class hypertension_screening(Ko):
    
    def __init__(self):
        super().__init__( __package__, [get_hypertension_screening_classification])
        self.add_endpoint("/check-inclusion", tags=["hypertension_screening"])
        
        

