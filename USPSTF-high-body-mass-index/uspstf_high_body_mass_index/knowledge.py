def get_bmi_category_knowledge(input):
    age = input['age']
    bmi_percentile = input['bmi_percentile']
    if age < 6 or age > 18 or bmi_percentile < 95:
        return {
            "inclusion": False
            }
    else:
        return {
            "inclusion": True,
            "recommendation": "The USPSTF recommends that clinicians provide or refer children and adolescents 6 years or older with a high body mass index (BMI) (≥95th percentile for age and sex) to comprehensive, intensive behavioral interventions.",
            "grade": "B",
            "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obesity-in-children-and-adolescents-screening"
            }