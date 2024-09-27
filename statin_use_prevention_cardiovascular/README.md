## Assumptions
The KO services can receive the following as input parameters
    - age (int): Age of the person.
    - has_cardiovascular_risk_factors (bool): Whether this person has CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) or not.
    - ten_year_CVD_risk (float): The probability that an individual will have a cardiovascular event (such as a heart attack or stroke) within the next 10 years (0 to 100).

## Knowledge Representation
The function get_statin_use at statin_use_prevention_cardiovascular/knowledge.py is the knowledge representation for this recommendation.

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
python statin_use_prevention_cardiovascular/cli_service/cli-service.py  -a 40 --has_cardiovascular_risk_factors -t 15  
python statin_use_prevention_cardiovascular/cli_service/cli-service.py  -a 40 --no-cardiovascular-risk-factors -t 15  
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x statin_use_prevention_cardiovascular/cli_service/cli-service.py
statin_use_prevention_cardiovascular/cli_service/cli-service.py -a 40 --has_cardiovascular_risk_factors -t 15
statin_use_prevention_cardiovascular/cli_service/cli-service.py -a 40 --no-cardiovascular-risk-factors -t 15
```