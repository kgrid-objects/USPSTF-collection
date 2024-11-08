def get_hypertension_screening_classification(age, hypertension):
    """
    Parameters:
    - age (int): Age of the person.
    - hypertension (bool): Indicated whether the person diagnosed for hypertension or not.
    """

    if age >= 18 and not hypertension:
        return {
            "inclusion": True,
            "title": "Hypertension in Adults: Screening",
            "recommendation": "The USPSTF recommends screening for hypertension in adults 18 years or older with office blood pressure measurement (OBPM). The USPSTF recommends obtaining blood pressure measurements outside of the clinical setting for diagnostic confirmation before starting treatment.",
            "grade": "A",
            "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening",
        }
    else:
        return {"inclusion": False, "title": "Hypertension in Adults: Screening"}
