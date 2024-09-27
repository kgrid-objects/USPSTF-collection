## Assumptions
It is assumed that KO services can receive the following as input parameters
    - age (int): Age of the person.
    - bmi (float): body mass index

## Knowledge Representation
The function get_diabetes_screening_classification at diabetes_screening/knowledge.py is the knowledge representation for this recommendation.

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
python diabetes_screening/cli_service/cli-service.py  -a 36 -b 26  
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x diabetes_screening/cli_service/cli-service.py
high_body_mass_index/cli_service/cli-service.py -a 36 -b 26
```