#!/usr/bin/env python3

import argparse
import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_statin_use

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="The USPSTF recommends that:\nFor adults aged 40 to 75 years who have 1 or more cardiovascular risk factors (ie, dyslipidemia, diabetes, hypertension, or smoking) and an estimated 10-year cardiovascular disease (CVD) risk of 10% or greater:\nInitiate a statin.\nGrade: B\n\nFor adults aged 40 to 75 years who have 1 or more cardiovascular risk factors (ie, dyslipidemia, diabetes, hypertension, or smoking) and an estimated 10-year CVD risk of 7.5% to less than 10%:\nSelectively offer a statin.\nGrade: C\n\nFor adults 76 years or older:\nThe evidence is insufficient to recommend for or against starting a statin.\nGrade: I",formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    parser.add_argument("-c", "--has_cardiovascular_risk_factors", type=bool, required=True, help="Whether this person has CVD risk factors (i.e dyslipidemia, diabetes, hypertension, or smoking) or not.")
    parser.add_argument("-t", "--ten_year_CVD_risk", type=float, required=True, help="The probability that an individual will have a cardiovascular event (such as a heart attack or stroke) within the next 10 years (0 to 100).")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate statin use inclusion
    result = get_statin_use(args.age, args.has_cardiovascular_risk_factors, args.ten_year_CVD_risk)
    
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()