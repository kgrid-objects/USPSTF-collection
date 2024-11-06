from hypertension_screening import hypertension_screening


def  apply(input):
    ko_instance = hypertension_screening()
    return ko_instance.execute(input)

