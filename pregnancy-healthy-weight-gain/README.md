Note: This KO is implemented using [Python SDK](https://github.com/kgrid/python-sdk) Ko_Execution class.

## Assumptions
It is assumed that KO services can receive the following as input parameters
    - pregnant (bool): Indicated if the person is pregnant.

## Knowledge Representation  
The function get_pregnancy_healthy_weight_gain_recommendation at pregnancy_healthy_weight_gain/knowledge.py is the knowledge representation for this recommendation.

## Usage
### Install KO
Installed the KO using pip install from code, whl file or from the repo like
```bash
pip install https://github.com/kgrid-objects/USPSTF-collection/archive/refs/heads/testSDK.zip#subdirectory=pregnancy-healthy-weight-gain
```

### Activator service
This KO does not implement Activator service.

### API service
This KO does not implement API service.

### CLI service
This KO does not implement CLI service.

### Use the knowledge object directly from the code
This section demonstrates how the knowledge embedded in this knowledge object can be utilized directly within the code of a client application. Once the `pregnancy-healthy-weight-gain` knowledge object is installed, the client application can import it as a package and access its modules and functions. The following code snippet imports knowledge object and runs its functions passing in a patient's data to obtain recommendation information.

This KO extends Ko_Execution class from kgrid SDK, so it inherits an execute method. The knowledge representation could be executed using both the `execute` method and the knowledge representation function directly from imported prevent_obesity_morbidity_mortality package.

```python
import json
from pregnancy_healthy_weight_gain import pregnancy_healthy_weight_gain

print(pregnancy_healthy_weight_gain.get_version())
print(json.dumps(pregnancy_healthy_weight_gain.execute({"pregnant":True}), indent=4))
print(json.dumps(pregnancy_healthy_weight_gain.get_pregnancy_healthy_weight_gain_recommendation(pregnant=True), indent=4))
```