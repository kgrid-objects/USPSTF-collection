#!/usr/bin/env python3

import argparse
import sys
import os
import json
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from knowledge import get_abdominal_aortic_aneurysm_screening

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="The USPSTF recommends that:\nFor men aged 65 to 75 years who have ever smoked:\nPerform 1-time screening for abdominal aortic aneurysm (AAA) with ultrasonography in men who have a history of smoking.\nGrade B\n\nFor men aged 65 to 75 years who have never smoked:\nSelectively offer screening to men who do not have a history of smoking, rather than routinely screening all men in this group\nGrade C\n\nFor women who have never smoked and have no family history of AAA:\nDo not screen women who have never smoked and do not have a family history of AAA.\nGrade D\n\nFor women aged 65 to 75 years who have ever smoked or have a family history of AAA:\nEvidence is insufficient to assess the balance of benefits and harms of screening for AAA with ultrasonography in women aged 65 to 75 years who have ever smoked or have a family history of AAA.\nGrade I",formatter_class=argparse.RawTextHelpFormatter)

    # Add arguments for weight and height
    parser.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    parser.add_argument("-g", "--gender", type=float, required=True, help="Gender of the individual (0 for women, 1 for men).")
   
    parser.add_argument("--has_never_smoked", action='store_true', help="Indicate if the person has never smoked.")
    parser.add_argument("--has_ever_smoked", action='store_false', dest='has_never_smoked', help="Indicate if the person has ever smoked.")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate statin use inclusion
    result = get_abdominal_aortic_aneurysm_screening(args.age, args.gender, args.has_never_smoked)
    
    print(json.dumps(result,indent=4))    

if __name__ == "__main__":
    main()