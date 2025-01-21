# USPSTF Knowledgebase
This package is implemended using Kgrid-SDK (python). The collection for this knowledgebase includes knowledge objects for recommendations grade A and B for adults from USPSTF recommendation categories Cardiovascular Disorders and Metabolic, nutritional, and Endocrine Conditions.

## usage
Use our Jupiter Notebook on our Google Colab page for [a step-by-Step tutorial on using USPSTF knowledgebase Package](https://colab.research.google.com/drive/1Ua3Kkc9HeeH1UbTQ6ab1GZ_sMIkdk8_f?usp=sharing) or follow the instructions below.

To use this python package, add it to your project's dependencies or install it in the python environment using
```bash
pip install https://github.com/kgrid/python-sdk/releases/download/1.0/uspstf_knowledgebase-0.1.9-py3-none-any.whl
```
or
```bash
poetry add https://github.com/kgrid/python-sdk/releases/download/1.0/uspstf_knowledgebase-0.1.9-py3-none-any.whl
```
Then import it in your code using
```python
from uspstf_knowledgebase import USPSTF_KnowledgeBase
```
Now you can call the `calculate_for_all` method from `USPSTF_KnowledgeBase` and pass patient data get the recommendations
```python
patient_data={
    "age":42,
    "bmi":33,
    "bmi_percentile":95.5,
    "has_never_smoked": True,
    "has_cardiovascular_risk_factors":True,
    "ten_year_CVD_risk":8,
    "hypertension":False
}

result = USPSTF_KnowledgeBase.calculate_for_all(patient_data)
print("execute all knowledge representations:\n",json.dumps(result, indent=4))
```

You can also access a specific knowledge object in the knowledgebase and call its knowledge representation functions. You will need the function name and signature for this.
```python
print("execute one knowledge representation:\n",USPSTF_KnowledgeBase.knowledge_objects['abdominal-aortic-aneurysm-screening'].get_abdominal_aortic_aneurysm_screening(age=20,gender=0,has_never_smoked=False))
```

You can also access other KO functions like get_metadata or get_version
```python
item=USPSTF_KnowledgeBase.knowledge_objects['cardiovascular-prevention-statin-use']
print("KO metadata: ",item.get_metadata())
print("KO version:  ",item.get_version())
```
