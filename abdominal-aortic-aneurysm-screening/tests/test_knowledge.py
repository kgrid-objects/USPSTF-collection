from abdominal_aortic_aneurysm_screening import abdominal_aortic_aneurysm_screening
def test_knowledge():
    assert not abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 30, gender= 1, has_never_smoked= False)["inclusion"] 
    assert not abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 80, gender= 1, has_never_smoked= False)["inclusion"]     
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 1, has_never_smoked= False)["inclusion"] 
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 1, has_never_smoked= False)["grade"] == "B"
    
    assert not abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 30, gender= 1, has_never_smoked= True)["inclusion"] 
    assert not abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 80, gender= 1, has_never_smoked= True)["inclusion"]  
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 1, has_never_smoked= True)["inclusion"] 
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 1, has_never_smoked= True)["grade"] == "C"

    assert not abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 30, gender= 0, has_never_smoked= False)["inclusion"] 
    assert not abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 80, gender= 0, has_never_smoked= False)["inclusion"]     
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 0, has_never_smoked= False)["inclusion"] 
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 0, has_never_smoked= False)["grade"] == "I"
    
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 30, gender= 0, has_never_smoked= True)["inclusion"] 
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 80, gender= 0, has_never_smoked= True)["inclusion"]  
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 0, has_never_smoked= True)["inclusion"] 
    assert abdominal_aortic_aneurysm_screening.get_abdominal_aortic_aneurysm_screening(age = 65, gender= 0, has_never_smoked= True)["grade"] == "D"





