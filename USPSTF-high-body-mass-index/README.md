

## assumptions
Inclusion criteria include children and adolescents 6 years or older. It is assumed that USPSTF recommendations consider adolescents to be people with age <=18.

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
python USPSTF-high-body-mass-index/uspstf_high_body_mass_index/cli_service/cli-service.py   
```

You can also make the python file executable using chmod to be able to execute it without using python command:
```bash
chmod +x USPSTF-high-body-mass-index/uspstf_high_body_mass_index/cli_service/cli-service.py
USPSTF-high-body-mass-index/uspstf_high_body_mass_index/cli_service/cli-service.py -a 17 -p 97
```