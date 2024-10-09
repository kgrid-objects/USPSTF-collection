def get_diabetes_screening_classification(age, bmi):
    """
    Parameters:
    - age (int): Age of the person.
    - bmi (float): body mass index.
    """
    
    if age >= 35 and age <=70 and bmi >= 25:
        return {
            "inclusion": True,
            "title": "Prediabetes and Type 2 Diabetes: Screening",
            "recommendation": "The USPSTF recommends screening for prediabetes and type 2 diabetes in adults aged 35 to 70 years who have overweight or obesity. Clinicians should offer or refer patients with prediabetes to effective preventive interventions.",
            "grade": "B",
            "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes"
            }
    else:
        return {
            "inclusion": False,
            "title": "Prediabetes and Type 2 Diabetes: Screening"
            }
        