#!/usr/bin/env python3

import argparse
import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_diabetes_screening_classification

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Adults aged 35 to 70 years who have overweight or obesity:\nThe USPSTF recommends screening for prediabetes and type 2 diabetes.  Clinicians should offer or refer patients with prediabetes to effective preventive interventions.\nGrade: B", formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    parser.add_argument("-b", "--bmi", type=float, required=True, help="body mass index")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate diabetes screening inclusion
    result = get_diabetes_screening_classification(args.age, args.bmi)
    
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()