## Assumptions
It is assumed that KO services can receive the following as input parameters
    - pregnant (bool): Indicated if the person is pregnant.

## Knowledge Representation  
The function get_pregnancy_healthy_weight_gain_recommendation at pregnancy_healthy_weight_gain/knowledge.py is the knowledge representation for this recommendation.

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
python pregnancy_healthy_weight_gain/cli_service/cli-service.py --pregnant
python pregnancy_healthy_weight_gain/cli_service/cli-service.py --not-pregnant
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x pregnancy_healthy_weight_gain/cli_service/cli-service.py
pregnancy_healthy_weight_gain/cli_service/cli-service.py --pregnant
pregnancy_healthy_weight_gain/cli_service/cli-service.py --not-pregnant
```