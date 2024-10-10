## Assumptions
The KO services can receive the following as input parameters
    - age (int): Age of the person.
    - has_cardiovascular_risk_factors (bool): Whether this person has CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) or not.

## Knowledge Representation
The function get_cardiovascular_disease_healthy_diet_activity_recommendation at cardiovascular_prevention_diet_activity/knowledge.py is the knowledge representation for this recommendation.

## Usage
### Activator service
create a local manifest file for the collection using python activator command line service and then run python activator pointing tto the collection path:
```bash
python-activator create-manifest --collection-path /path/to/collection/USPSTF-collection
python-activator run --collection-path /path/to/collection/USPSTF-collection
```

### CLI service
Here is an example of using the cli
```bash
python cardiovascular_prevention_diet_activity/cli_service/cli_service.py  -a 40 --has_cardiovascular_risk_factors
python cardiovascular_prevention_diet_activity/cli_service/cli_service.py  -a 40 --no_cardiovascular_risk_factors
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x cardiovascular_prevention_diet_activity/cli_service/cli_service.py
cardiovascular_prevention_diet_activity/cli_service/cli_service.py -a 40 --has_cardiovascular_risk_factors
cardiovascular_prevention_diet_activity/cli_service/cli_service.py -a 40 --no_cardiovascular_risk_factors
```