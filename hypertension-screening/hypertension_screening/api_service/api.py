from hypertension_screening import hypertension_screening

ko_instance = hypertension_screening()
app = ko_instance.app

# # only runs virtual server when running this .py file directly for debugging
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
