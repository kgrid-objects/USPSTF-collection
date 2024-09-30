#!/usr/bin/env python3

import argparse
import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_obesity_recommendation

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Adults with a BMI ≥30:\nThe USPSTF recommends that clinicians offer or refer to intensive, multicomponent behavioral interventions.\nGrade: B", formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    parser.add_argument("-b", "--bmi", type=float, required=True, help="body mass index")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate diabetes screening inclusion
    result = get_obesity_recommendation(args.age, args.bmi)
    
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()