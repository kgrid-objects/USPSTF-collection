#!/usr/bin/env python3

import argparse
import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_cardiovascular_disease_healthy_diet_activity_recommendation

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="The USPSTF recommends that:\nFor adults 18 years or older at increased risk of cardiovascular disease (CVD):\nProvide behavioral counseling to promote a healthy diet and physical activity.\nGrade: B",formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    parser.add_argument("-c", "--has_cardiovascular_risk_factors", action='store_true', help="Indicate if the person has cardiovascular risk factors (e.g., dyslipidemia, diabetes, hypertension, or smoking).")
    parser.add_argument("--no_cardiovascular_risk_factors", action='store_false', dest='has_cardiovascular_risk_factors', help="Indicate if the person does NOT have cardiovascular risk factors.")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate statin use inclusion
    result = get_cardiovascular_disease_healthy_diet_activity_recommendation(args.age, args.has_cardiovascular_risk_factors)
    
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()