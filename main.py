import os

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

from ml.data import apply_label, process_data
from ml.model import inference, load_model


# DO NOT MODIFY
class Data(BaseModel):
    age: int = Field(..., example=37)
    workclass: str = Field(..., example="Private")
    fnlgt: int = Field(..., example=178356)
    education: str = Field(..., example="HS-grad")
    education_num: int = Field(..., example=10, alias="education-num")
    marital_status: str = Field(
        ..., example="Married-civ-spouse", alias="marital-status"
    )
    occupation: str = Field(..., example="Prof-specialty")
    relationship: str = Field(..., example="Husband")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    capital_gain: int = Field(..., example=0, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., example=40, alias="hours-per-week")
    native_country: str = Field(..., example="United-States",
                                alias="native-country")


# Enter the path to your project directory
project_path = os.path.dirname(__file__)

# Path for the saved encoder
path = os.path.join(project_path, 'model', 'encoder.pkl')
encoder = load_model(path)

# Path for the saved model
path = os.path.join(project_path, 'model', 'model.pkl')
model = load_model(path)

# Create a RESTful API using FastAPI
app = FastAPI()


# Create a GET on the root giving a welcome message
@app.get("/")
async def get_root():
    """ Say hello!"""
    return {'greeting': 'Hello, welcome to G.L.\'s model inference API!'}


# TODO: create a POST on a different path that does model inference
@app.post("/data/")
def post_inference(data: Data):
    # DO NOT MODIFY: turn the Pydantic model into a dict.
    data_dict = data.model_dump()
    # data_dict = data.dict()
    # DO NOT MODIFY: clean up the dict to turn it into a Pandas DataFrame.
    # The data has names with hyphens and Python does not allow those as
    # variable names.
    # Here it uses the functionality of FastAPI/Pydantic/etc to deal with this.
    data = {k.replace("-", "_"): [v] for k, v in data_dict.items()}
    data = pd.DataFrame.from_dict(data)

    cat_features = [
        "workclass",
        "education",
        "marital_status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native_country",
    ]
    data_processed, _, _, _ = process_data(
        # your code here
        # use data as data input
        # use training = False
        # do not need to pass lb as input
        data,
        categorical_features=cat_features,
        training=False,
        encoder=encoder
        # label=None to indicate that we are not training but inferring
    )
    # Predict the result using data_processed
    inference_result = inference(model, data_processed)
    # Apply label to the inference result
    result = apply_label(inference_result)

    return {"result": result}
