from hypertension_screening import hypertension_screening
from hypertension_screening import apply

version = "v1.8"
def test_get_version():
    assert version == hypertension_screening.get_version()


def test_metadata():
   assert version == hypertension_screening.get_metadata().get("version", "Unknown version")


def test_execute():
    assert (
        "Hypertension in Adults: Screening"
        == hypertension_screening.execute({"age": 20, "hypertension": False})["title"]
    )


def test_activator_function():
    assert (
        "Hypertension in Adults: Screening"
        == apply({"age": 20, "hypertension": False})["title"]
    )


def test_direct_call():
    assert hypertension_screening.get_hypertension_screening_classification(
         17 , False
    ) == {"inclusion": False, "title": "Hypertension in Adults: Screening"}
    
