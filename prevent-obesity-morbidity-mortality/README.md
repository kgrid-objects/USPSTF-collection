Note: This KO is implemented using [Python SDK](https://github.com/kgrid/python-sdk) Ko class.

## Assumptions
It is assumed that KO services can receive the following as input parameters
    - age (int): Age of the person.
    - bmi (float): body mass index

## Knowledge Representation
The function get_obesity_recommendation at prevent_obesity_morbidity_mortality/knowledge.py is the knowledge representation for this recommendation.

## Usage
### Activator service
This KO does not implement Activator service.

### Install KO
Installed the KO using pip install from code, whl file or from the repo like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=prevent-obesity-morbidity-mortality
```
### API service
This KO does not implement API service.

### CLI service
This KO does not implement CLI service.

### Use the knowledge object directly from the code
This section demonstrates how the knowledge embedded in this knowledge object can be utilized directly within the code of a client application. Once the `prevent-obesity-morbidity-mortality` knowledge object is installed, the client application can import it as a package and access its modules and functions. The following code snippet imports knowledge object and runs its functions passing in a patient's data to obtain recommendation information. 

This KO extends Ko class from kgrid SDK, so it does not have an execute method but the knowledge representation could still be accessed directly from imported prevent_obesity_morbidity_mortality package.

```python
import json
from prevent_obesity_morbidity_mortality import prevent_obesity_morbidity_mortality

print(prevent_obesity_morbidity_mortality.get_version())
print(json.dumps(prevent_obesity_morbidity_mortality.get_obesity_recommendation(age=20,bmi=30), indent=4))
```