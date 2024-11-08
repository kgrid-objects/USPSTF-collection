## Assumptions
This KO is implemented using [Python SDK](https://github.com/kgrid/python-sdk)

The KO services can receive the following as input parameters
    - age (int): Age of the person.
    - has_cardiovascular_risk_factors (bool): Whether this person has CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) or not.

## Knowledge Representation
The function get_cardiovascular_disease_healthy_diet_activity_recommendation at cardiovascular_prevention_diet_activity/knowledge.py is the knowledge representation for this recommendation.

## Usage
### Activator service
Follow the instruction at [python activator](https://github.com/kgrid/python-activator/blob/main/README.md) repo to install python activator and see different ways of running the python activator and activating this KO.

One way o activate this KO is to clone the USPSTF collection and use the local_manifest.json file: 
```bash
python-activator run --collection-path /path/to/collection/USPSTF-collection
```

You can also activate this KO from a zip file and a manifest file that point to it:
```bash
python-activator run --manifest-path https://github.com/kgrid-objects/USPSTF-collection/releases/download/1.0/manifest.json
```

Then use the swagger editor at `http://127.0.0.1:8000/docs` to access python activator endpoints and documentation how to use the KO.

You can also send post requests to `http://localhost:8000/endpoints/cardiovascular-prevention-diet-activity/check-inclusion` with a request body like
```json
{
"age":20,
"has_cardiovascular_risk_factors":true
}
```
to access the `cardiovascular-prevention-diet-activity` KO.

### Install KO
Installed the KO using pip install from code, whl file or from the repo like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=cardiovascular-prevention-diet-activity
```
### API service
Once the KO is installed you can run the API service using
```bash
uvicorn cardiovascular_prevention_diet_activity.cardiovascular_prevention_diet_activity:app
```

Then use the swagger editor at `http://127.0.0.1:8000` or send post requests to `http://127.0.0.1:8000/check-inclusion` with a request body like
```json
{
"age":20,
"has_cardiovascular_risk_factors":true
}
``` 

### CLI service
Once the KO is installed use the cli service like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=cardiovascular-prevention-diet-activity
cardiovascular-prevention-diet-activity --a 30 --has_cardiovascular_risk_factors
```
### Use the knowledge object directly from the code
This section demonstrates how the knowledge embedded in this knowledge object can be utilized directly within the code of a client application. Once the `cardiovascular-prevention-diet-activity` knowledge object is installed, the client application can import it as a package and access its modules and functions. The following code snippet imports knowledge object and runs its functions passing in a patient's data to obtain recommendation information.

```python
import json
from cardiovascular_prevention_diet_activity import cardiovascular_prevention_diet_activity

ko_instance = cardiovascular_prevention_diet_activity()
print(ko_instance.get_version())
print(json.dumps(ko_instance.execute({"age":20,"has_cardiovascular_risk_factors":True}), indent=4))
```