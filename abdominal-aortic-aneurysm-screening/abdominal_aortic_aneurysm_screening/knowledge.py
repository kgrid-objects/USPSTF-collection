def get_abdominal_aortic_aneurysm_screening(age, gender, has_never_smoked):
    """
    Parameters:
    - age (int): Age of the person.
    - gender (int): Gender of the individual (0 for women, 1 for men).    
    - has_never_smoked (bool): Whether this person has never smoked or not.
    """
    
    if gender == 1:
        if age >= 65 and age <= 75 and not has_never_smoked:        
            return {
                "inclusion": True,
                "recommendation": "The USPSTF recommends 1-time screening for abdominal aortic aneurysm (AAA) with ultrasonography in men aged 65 to 75 years who have ever smoked.",
                "grade": "B",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/abdominal-aortic-aneurysm-screening"
                }
        elif age >= 65 and age <= 75 and has_never_smoked:  
            return {
                "inclusion": True,
                "recommendation": "The USPSTF recommends that clinicians selectively offer screening for AAA with ultrasonography in men aged 65 to 75 years who have never smoked rather than routinely screening all men in this group. Evidence indicates that the net benefit of screening all men in this group is small. In determining whether this service is appropriate in individual cases, patients and clinicians should consider the balance of benefits and harms on the basis of evidence relevant to the patient's medical history, family history, other risk factors, and personal values.",
                "grade": "C",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/abdominal-aortic-aneurysm-screening"
                }
    elif gender == 0:
        if has_never_smoked:        
            return {
                "inclusion": True,
                "recommendation": "The USPSTF recommends against routine screening for AAA with ultrasonography in women who have never smoked and have no family history of AAA.",
                "grade": "D",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/abdominal-aortic-aneurysm-screening"
                }
        elif age >= 65 and age <= 75 and not has_never_smoked:  
            return {
                "inclusion": True,
                "recommendation": "The USPSTF concludes that the current evidence is insufficient to assess the balance of benefits and harms of screening for AAA with ultrasonography in women aged 65 to 75 years who have ever smoked or have a family history of AAA.",
                "grade": "I",
                "URL": "https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/abdominal-aortic-aneurysm-screening"
                }

        
    return {
        "inclusion": False    
        }
        