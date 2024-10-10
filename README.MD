# USPSTF Recommendations Collection

## Knowledge objects
This collection implements 8 knowledge objects, using [KGrid 2.0](https://github.com/kgrid/specs/blob/master/docs/kgrid-knowledge-objects.md) model, for the following published USPSTF recommendations:

|Type|Year|Topic Name|Age Group|Grade|Category|Links|
|-|-|-|-|-|-|-|
| Screening | 2019 | Abdominal Aortic Aneurysm: Screening| Adult, Senior | B, C, D, I| Cardiovascular Disorders (Heart and Vascular Diseases)| [Knowledge object information page](),[USPSTF page]() |
| Counseling| 2020 | Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions | Adult, Senior | B | Cardiovascular Disorders (Heart and Vascular Diseases), Development and Behavior | [Knowledge object information page](/abdominal-aortic-aneurysm-screening/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/abdominal-aortic-aneurysm-screening) |
| Counseling| 2021 | Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions | Adolescent, Adult | B | Development and Behavior, Metabolic, nutritional, and Endocrine Conditions, Obstetric and Gynecologic Conditions | [Knowledge object information page](/pregnancy-healthy-weight-gain/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/healthy-weight-and-weight-gain-during-pregnancy-behavioral-counseling-interventions)|
| Counseling| 2024 | High Body Mass Index in Children and Adolescents: Interventions | Adolescent, Pediatric | B | Metabolic, nutritional, and Endocrine Conditions | [Knowledge object information page](/high-body-mass-index/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obesity-in-children-and-adolescents-screening) |
| Screening | 2021 | Hypertension in Adults: Screening | Adult, Senior | A | Cardiovascular Disorders (Heart and Vascular Diseases)| [Knowledge object information page](/hypertension-screening/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening) |
| Screening | 2021 | Prediabetes and Type 2 Diabetes: Screening| Adult, Senior | B | Metabolic, nutritional, and Endocrine Conditions | [Knowledge object information page](/diabetes-screening/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes) |
| Preventive medication| 2022 | Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication | Adult, Senior | B, C, I | Cardiovascular Disorders (Heart and Vascular Diseases)| [Knowledge object information page](/cardiovascular-prevention-statin-use/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication#fullrecommendationstart) |
| Counseling| 2018 | Weight Loss to Prevent Obesity-Related Morbidity and Mortality in Adults: Behavioral Interventions | Adult, Senior | B | Metabolic, nutritional, and Endocrine Conditions | [Knowledge object information page](/prevent-obesity-morbidity-mortality/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/obesity-in-adults-interventions) |

See knowledge object information page or the USPSTF page link for more detail on each knowledge object.

## Demo app
The USPSTF collection [demo app](/demo/) utilizes the knowledge objects in this repository to deliver precision prevention, providing tailored preventive recommendations for individual patients. 

For development, run the following in demo folder to make a virtual local server:
```
python -m http.server 8001
```

Then access the demo page using `http://localhost:8001/`

## How to use these knowledge objects

### Using [python activator](https://github.com/kgrid/python-activator)
Install the python activator. Run and point it to the manifest file in this repo:

```
pip install "python-activator[cli]@https://github.com/kgrid/python-activator/releases/download/0.8/python_activator-0.8-py3-none-any.whl"

ORG_KGRID_PYTHON_ACTIVATOR_MANIFEST_PATH=https://github.com/kgrid-objects/USPSTF-collection/releases/download/1.0/manifest.json python-activator run
```

Then you can access the python activator at 

Try the [python activator with USPSTF collection here](https://uspstf-collection-b68f2ecc738e.herokuapp.com/docs).

### Using command line interface
Install the knowledge object that you would like to use for example abdominal-aortic-aneurysm-screening:
```batch
!pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/main.zip#subdirectory=abdominal-aortic-aneurysm-screening
```

Then run the command and pass the input values for a patient:
```
!abdominal-aortic-aneurysm-screening -a 42 -g 1
```
