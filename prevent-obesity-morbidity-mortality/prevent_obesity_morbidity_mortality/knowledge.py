def get_obesity_recommendation(age, bmi):
    """
    Parameters:
    - age (int): Age of the person.
    - bmi (float): body mass index.
    """
    
    if age >= 18 and bmi >= 30:
        return {
            "inclusion": True,
            "recommendation": "The USPSTF recommends that clinicians offer or refer adults with a body mass index (BMI) of 30 or higher (calculated as weight in kilograms divided by height in meters squared) to intensive, multicomponent behavioral interventions.",
            "grade": "B",
            "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/obesity-in-adults-interventions"
            }
    else:
        return {
            "inclusion": False
            }
        