Note: This KO is implemented using [Python SDK](https://github.com/kgrid/python-sdk)

## Assumptions
It is assumed that KO services can receive the following as input parameters
    - age (int): Age of the person.
    - bmi (float): body mass index

## Knowledge Representation
The function get_diabetes_screening_classification at diabetes_screening/knowledge.py is the knowledge representation for this recommendation.

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

You can also send post requests to `http://localhost:8000/endpoints/diabetes-screening/check-inclusion` with a request body like
```json
{
"age":35,
"bmi":30
}
```
to access the `diabetes-screening` KO.

### Install KO
Installed the KO using pip install from code, whl file or from the repo like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=diabetes-screening
```
### API service
Once the KO is installed you can run the API service using
```bash
pip install uvicorn 
uvicorn diabetes_screening.diabetes_screening:app
```

Then use the swagger editor at `http://127.0.0.1:8000` or send post requests to `http://127.0.0.1:8000/check-inclusion` with a request body like
```json
{
"age":35,
"bmi":30
}
``` 

### CLI service
Once the KO is installed use the cli service like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=diabetes-screening
diabetes-screening --a 35 --b 30
```
### Use the knowledge object directly from the code
This section demonstrates how the knowledge embedded in this knowledge object can be utilized directly within the code of a client application. Once the `diabetes-screening` knowledge object is installed, the client application can import it as a package and access its modules and functions. The following code snippet imports knowledge object and runs its functions passing in a patient's data to obtain recommendation information.

```python
import json
from diabetes_screening import diabetes_screening

print(diabetes_screening.get_version())
print(json.dumps(diabetes_screening.execute({"age":35,"bmi": 30}), indent=4))
```