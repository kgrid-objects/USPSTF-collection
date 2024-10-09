def get_high_body_mass_index_classification(age, bmi_percentile):
    """
    Parameters:
    - age (int): Age of the person.
    - bmi_percentile (float): bmi percentile for age and sex.
    """
    
    if age < 6 or age > 18 or bmi_percentile < 95:
        return {
            "inclusion": False,
            "title": "High Body Mass Index in Children and Adolescents: Interventions"
            }
    else:
        return {
            "inclusion": True,
            "title": "High Body Mass Index in Children and Adolescents: Interventions",
            "recommendation": "The USPSTF recommends that clinicians provide or refer children and adolescents 6 years or older with a high body mass index (BMI) (≥95th percentile for age and sex) to comprehensive, intensive behavioral interventions.",
            "grade": "B",
            "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obesity-in-children-and-adolescents-screening"
            }