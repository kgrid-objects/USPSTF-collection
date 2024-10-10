## Assumptions
The KO services can receive the following as input parameters
    - age (int): Age of the person.
    - has_cardiovascular_risk_factors (bool): Whether this person has CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) or not.
    - ten_year_CVD_risk (float): The probability that an individual will have a cardiovascular event (such as a heart attack or stroke) within the next 10 years (0 to 100).

## Knowledge Representation
The function get_statin_use at cardiovascular_prevention_statin_use/knowledge.py is the knowledge representation for this recommendation.

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
python cardiovascular_prevention_statin_use/cli_service/cli_service.py  -a 40 --has_cardiovascular_risk_factors -t 15  
python cardiovascular_prevention_statin_use/cli_service/cli_service.py  -a 40 --no_cardiovascular_risk_factors -t 15  
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x cardiovascular_prevention_statin_use/cli_service/cli_service.py
cardiovascular_prevention_statin_use/cli_service/cli_service.py -a 40 --has_cardiovascular_risk_factors -t 15
cardiovascular_prevention_statin_use/cli_service/cli_service.py -a 40 --no_cardiovascular_risk_factors -t 15
```