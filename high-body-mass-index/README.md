Note: This KO is implemented using [Python SDK](https://github.com/kgrid/python-sdk)

## Assumptions
Inclusion criteria include children and adolescents 6 years or older. It is assumed that USPSTF recommendations consider adolescents to be people with age <=18.

It is assumed that KO services can receive the following as input parameters
    - age (int): Age of the person.
    - bmi_percentile (float): bmi percentile for age and sex.

## Knowledge Representation
The function get_high_body_mass_index_classification at high_body_mass_index/knowledge.py is the knowledge representation for this recommendation.

## Usage
### Activator service
Follow the instruction at [python activator](https://github.com/kgrid/python-activator/blob/main/README.md) repo to install python activator and see different ways of running the python activator and activating this KO.

One way to activate this KO is to clone the USPSTF collection and use the local_manifest.json file: 
```bash
python-activator run --collection-path /path/to/collection/USPSTF-collection
```

You can also activate this KO from a zip file and a manifest file that point to it:
```bash
python-activator run --manifest-path https://github.com/kgrid-objects/USPSTF-collection/releases/download/1.0/manifest.json
```

Then use the swagger editor at `http://127.0.0.1:8000/docs` to access python activator endpoints and documentation how to use the KO.

You can also send post requests to `http://localhost:8000/endpoints/high-body-mass-index/check-inclusion` with a request body like
```json
{
"age":17,
"bmi_percentile":95
}
```
to access the `high-body-mass-index` KO.

### Install KO
Installed the KO using pip install from code, whl file or from the repo like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=high-body-mass-index
```
### API service
Once the KO is installed you can run the API service using
```bash
pip install uvicorn 
uvicorn high_body_mass_index.high_body_mass_index:app
```

Then use the swagger editor at `http://127.0.0.1:8000` or send post requests to `http://127.0.0.1:8000/check-inclusion` with a request body like
```json
{
"age":17,
"bmi_percentile":95
}
``` 

### CLI service
Once the KO is installed use the cli service like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=high-body-mass-index
high-body-mass-index --a 17 -p 95
```
### Use the knowledge object directly from the code
This section demonstrates how the knowledge embedded in this knowledge object can be utilized directly within the code of a client application. Once the `high-body-mass-index` knowledge object is installed, the client application can import it as a package and access its modules and functions. The following code snippet imports knowledge object and runs its functions passing in a patient's data to obtain recommendation information.

```python
import json
from high_body_mass_index import high_body_mass_index

ko_instance = high_body_mass_index()
print(ko_instance.get_version())
print(json.dumps(ko_instance.execute({"age":17,"bmi_percentile": 95}), indent=4))
```