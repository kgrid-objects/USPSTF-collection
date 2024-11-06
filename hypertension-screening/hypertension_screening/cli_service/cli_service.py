from hypertension_screening import hypertension_screening
def main():
    ko_instance = hypertension_screening()
    ko_instance.define_cli()
    ko_instance.add_argument("-a", "--age", type=float, required=True, help="Age of the person")
    ko_instance.add_argument("-t", "--hypertension", action="store_true", help="Indicate if the person is diagnosed with hypertension.")
    ko_instance.add_argument("--no-hypertension", action="store_false", dest="hypertension", help="Indicate if the person is NOT diagnosed with hypertension.")
    ko_instance.execute_cli()

if __name__ == "__main__":
    main()

