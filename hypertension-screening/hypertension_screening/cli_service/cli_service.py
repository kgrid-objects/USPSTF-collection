#!/usr/bin/env python3

import argparse
import sys
import os
import json


parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_hypertension_screening_classification

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Adults 18 years or older without known hypertension:\nThe USPSTF recommends screening for hypertension in adults 18 years or older with office blood pressure measurement (OBPM). The USPSTF recommends obtaining blood pressure measurements outside of the clinical setting for diagnostic confirmation before starting treatment.\nGrade: A", formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    parser.add_argument("-t", "--hypertension", action='store_true', help="Indicate if the person is diagnosed with hypertension.")
    parser.add_argument("--no-hypertension", action='store_false', dest='hypertension', help="Indicate if the person is NOT diagnosed with hypertension.")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate hypertension screening inclusion
    result = get_hypertension_screening_classification(args.age, args.hypertension)
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()