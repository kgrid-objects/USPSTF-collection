---
layout: default
title: KOIO
permalink: /index.html
---

# [USPSTF Recommendations Collection](https://kgrid-objects.github.io/USPSTF-collection/)

## Knowledge objects
This collection implements 8 knowledge objects, using [KGrid 2.0](https://github.com/kgrid/specs/blob/master/docs/kgrid-knowledge-objects.md) model, for the following published USPSTF recommendations:

|Type|Year|Topic Name|Age Group|Grade|Category|Links|
|-|-|-|-|-|-|-|
| Screening | 2019 | Abdominal Aortic Aneurysm: Screening| Adult, Senior | B, C, D, I| Cardiovascular Disorders (Heart and Vascular Diseases)| [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/abdominal-aortic-aneurysm-screening/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/abdominal-aortic-aneurysm-screening) |
| Counseling| 2020 | Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions | Adult, Senior | B | Cardiovascular Disorders (Heart and Vascular Diseases), Development and Behavior | [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/cardiovascular-prevention-diet-activity/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/healthy-diet-and-physical-activity-counseling-adults-with-high-risk-of-cvd) |
| Counseling| 2021 | Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions | Adolescent, Adult | B | Development and Behavior, Metabolic, nutritional, and Endocrine Conditions, Obstetric and Gynecologic Conditions | [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/pregnancy-healthy-weight-gain/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/healthy-weight-and-weight-gain-during-pregnancy-behavioral-counseling-interventions)|
| Counseling| 2024 | High Body Mass Index in Children and Adolescents: Interventions | Adolescent, Pediatric | B | Metabolic, nutritional, and Endocrine Conditions | [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/high-body-mass-index/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obesity-in-children-and-adolescents-screening) |
| Screening | 2021 | Hypertension in Adults: Screening | Adult, Senior | A | Cardiovascular Disorders (Heart and Vascular Diseases)| [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/hypertension-screening/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening) |
| Screening | 2021 | Prediabetes and Type 2 Diabetes: Screening| Adult, Senior | B | Metabolic, nutritional, and Endocrine Conditions | [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/diabetes-screening/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes) |
| Preventive medication| 2022 | Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication | Adult, Senior | B, C, I | Cardiovascular Disorders (Heart and Vascular Diseases)| [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/cardiovascular-prevention-statin-use/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication#fullrecommendationstart) |
| Counseling| 2018 | Weight Loss to Prevent Obesity-Related Morbidity and Mortality in Adults: Behavioral Interventions | Adult, Senior | B | Metabolic, nutritional, and Endocrine Conditions | [Knowledge object information page](https://kgrid-objects.github.io/USPSTF-collection/prevent-obesity-morbidity-mortality/),[USPSTF page](https://www.uspreventiveservicestaskforce.org/uspstf/index.php/recommendation/obesity-in-adults-interventions) |

See knowledge object information page or the USPSTF page link for more detail on each knowledge object.

## Demo app
### Demo app 1, using a python activator knowledgebase
The USPSTF collection [Demo App 1](https://kgrid-objects.github.io/USPSTF-collection/demo/), located in the [demo folder](./demo/index.html), leverages the knowledge objects in this repository via a [Python Activator Knowledgebase deployed on Heroku](https://uspstf-collection-b68f2ecc738e.herokuapp.com). This app delivers precision prevention by providing tailored preventive recommendations for individual patients. 

#### Running the demo app 1 localy
This requires a running activator that activates the USPSTF knowledge objects, and the link is set in the JavaScript code of the demo app. For development purposes, open the [demo](./demo) folder in terminal and run a local virtual server with the following command:
```bash
python -m http.server 8001
```

Then access the demo page at:
`http://localhost:8001/`

### Demo app 2, using an SDK-built Knowledgebase
This demo app integrates the USPSTF Collection knowledge objects, included in a knowledgebase, directly in the code. The knowledgebase is created using the [KGrid-SDK](https://github.com/kgrid/python-sdk?tab=readme-ov-file#create-a-collection-using-kgrid_sdkcollection) and (published as a python package)[https://pypi.org/project/kgrid-sdk/], eliminating the need for a separate deployment.

#### Running the demo app 2 locally in a development environment 
Follow these steps to run the app locally:
1. Change the active directory to the [root of the app](./demo/sdk_demo/)
```bash
cd path/to/demo/app
```

2. Activate the Poetry virtual environment
```bash
poetry shell
```

3. Install project dependencies
```bash
poetry install
```

4. Set the `FLASK_APP` environment variable with the path to the Flask app definition 
```bash
export FLASK_APP=sdk_demo.app:app 
```

5. Execute the Flask app 
```bash
flask run 
```
Then, access the demo app at http://127.0.0.1:5000 in your browser.

## How to use these knowledge objects
### Knowledge object information page
To open knowledge object information page, open a knowledge object directory (we recommend using [Visual Studio Code](https://code.visualstudio.com/)). Then run a localvirtual server using
```bash
python -m http.server 8001
```
and the access http://localhost:8001/ in your browser.

### Using [python activator](https://github.com/kgrid/python-activator)
Install the python activator. Run and point it to the manifest file in this repo:

```bash
pip install "python-activator[cli]@https://github.com/kgrid/python-activator/releases/download/0.8/python_activator-0.8-py3-none-any.whl"

ORG_KGRID_PYTHON_ACTIVATOR_MANIFEST_PATH=https://github.com/kgrid-objects/USPSTF-collection/releases/download/1.0/manifest.json python-activator run
```

Then you can access the python activator at 
`http://127.0.0.1:8000`

You can try the [python activator with USPSTF collection here](https://uspstf-collection-b68f2ecc738e.herokuapp.com/docs).

### Using command line interface
For the knowledge objects which implement a CLI service, install the knowledge object that you would like to use, for example:
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/main.zip#subdirectory=abdominal-aortic-aneurysm-screening
```

Then run the command and pass the input values for a patient:
```bash
abdominal-aortic-aneurysm-screening -a 42 -g 1
```

### Using API service
Install the KO that you want to use.
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/main.zip#subdirectory=abdominal-aortic-aneurysm-screening
```

Install `uvicorn` in your environment
```bash
pip install uvicorn
```

Then use `uvicorn` to run the api service, for example
```bash
uvicorn abdominal_aortic_aneurysm_screening.abdominal_aortic_aneurysm_screening:app
```

Then you can use the swagger editor at `http://127.0.0.1:8000` or send post requests to `http://127.0.0.1:8000/check-inclusion` with a request body like
```json
{
"age":20,
"gender": 0,
"has_never_smoked":false
}
``` 


### Using the knowledge objects directly in the code 
See the [KGrid python SDK](https://github.com/kgrid/python-sdk?tab=readme-ov-file#create-a-collection-using-kgrid_sdkcollection) for an example of how to use KGrid SDK to create a knowledgebase utilizing USPSTF collection knowledge objects directly in the code and how to use the knowledgebase in an application.
