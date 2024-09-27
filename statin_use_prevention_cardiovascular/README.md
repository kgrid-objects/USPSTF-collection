## Assumptions

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
python statin_use_prevention_cardiovascular/cli_service/cli-service.py  -a 40 -c True -t 15  
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x statin_use_prevention_cardiovascular/cli_service/cli-service.py
statin_use_prevention_cardiovascular/cli_service/cli-service.py -a 40 -c True -t 15
```