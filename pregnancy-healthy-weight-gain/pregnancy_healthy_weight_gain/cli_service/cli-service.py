#!/usr/bin/env python3

import argparse
import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_pregnancy_healthy_weight_gain_recommendation

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="For pregnant adolescents and adults:\nThe USPSTF recommends that clinicians offer effective behavioral counseling interventions aimed at promoting healthy weight gain and preventing excess gestational weight gain in pregnancy.\nGrade B", formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-p", "--pregnant", action='store_true', help="Indicate if the person is pregnant.")
    parser.add_argument("--not-pregnant", action='store_false', dest='pregnant', help="Indicate if the person is NOT pregnant.")

    # Parse the arguments
    args = parser.parse_args()

    # check recommendation inclusion
    result = get_pregnancy_healthy_weight_gain_recommendation(args.pregnant)
    
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()