#!/usr/bin/env python3

import argparse
import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_high_body_mass_index_classification

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Children and adolescents 6 years or older:\nThe USPSTF recommends that clinicians should provide or refer children and adolescents 6 years or older with a high body mass index (BMI) (≥95th percentile for age and sex) to comprehensive, intensive behavioral interventions.\nGrade: B", formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    parser.add_argument("-p", "--bmi_percentile", type=float, required=True, help="bmi percentile for age and sex")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate high BMI inclusion
    result = get_high_body_mass_index_classification(args.age, args.bmi_percentile)
    
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()