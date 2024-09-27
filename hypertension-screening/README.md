## Assumptions
It is assumed that KO services can receive the following as input parameters
    - age (int): Age of the person.
    - hypertension (bool): Indicated whether the person diagnosed for hypertension or not.

## Knowledge Representation
The function get_hypertension_screening_classification at hypertension_screening/knowledge.py is the knowledge representation for this recommendation.

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
python hypertension_screening/cli_service/cli-service.py  -a 30 --hypertension
python hypertension_screening/cli_service/cli-service.py  -a 30 --no-hypertension
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x hypertension_screening/cli_service/cli-service.py
hypertension_screening/cli_service/cli-service.py -a 30 --hypertension
hypertension_screening/cli_service/cli-service.py -a 30 --no-hypertension
```