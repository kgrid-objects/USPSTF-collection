## Assumptions
The KO services can receive the following as input parameters
    - age (int): Age of the person.
    - gender (int): Gender of the individual (0 for women, 1 for men).    
    - has_never_smoked (bool): Whether this person has never smoked or not.
## Knowledge Representation
The function get_abdominal_aortic_aneurysm_screening at abdominal_aortic_aneurysm_screening/knowledge.py is the knowledge representation for this recommendation.

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
python abdominal_aortic_aneurysm_screening/cli_service/cli_service.py  -a 65 -g 1 --has_never_smoked  
python abdominal_aortic_aneurysm_screening/cli_service/cli_service.py  -a 65 -g 1 --has_ever_smoked  
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x abdominal_aortic_aneurysm_screening/cli_service/cli_service.py
abdominal_aortic_aneurysm_screening/cli_service/cli_service.py -a 65 -g 1 --has_never_smoked  
abdominal_aortic_aneurysm_screening/cli_service/cli_service.py -a 65 -g 1 --has_ever_smoked  
```