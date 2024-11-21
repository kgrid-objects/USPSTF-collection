from hypertension_screening import hypertension_screening
from hypertension_screening import apply


def test_get_version():
    version = hypertension_screening.get_version()
    assert version == "v1.6"


def test_metadata():
    version = hypertension_screening.get_metadata().get("version", "Unknown version")
    assert version == "v1.6"


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
    
