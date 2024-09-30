from ..knowledge import get_abdominal_aortic_aneurysm_screening

def apply(input):
    return get_abdominal_aortic_aneurysm_screening(input["age"], input["gender"], input["has_never_smoked"])

