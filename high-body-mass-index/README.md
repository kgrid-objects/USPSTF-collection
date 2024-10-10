## Assumptions
Inclusion criteria include children and adolescents 6 years or older. It is assumed that USPSTF recommendations consider adolescents to be people with age <=18.

It is assumed that KO services can receive the following as input parameters
    - age (int): Age of the person.
    - bmi_percentile (float): bmi percentile for age and sex.

## Knowledge Representation
The function get_high_body_mass_index_classification at high_body_mass_index/knowledge.py is the knowledge representation for this recommendation.

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
python high_body_mass_index/cli_service/cli_service.py  -a 17 -p 97  
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x high_body_mass_index/cli_service/cli_service.py
high_body_mass_index/cli_service/cli_service.py -a 17 -p 97
```