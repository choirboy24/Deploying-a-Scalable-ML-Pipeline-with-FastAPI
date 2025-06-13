import math
import pandas as pd
from train_model import train, test, data  # Adjust the import based on your project structure
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_function_return():
    """
    # Unit test to check if the function returns the correct data type

    """
    assert isinstance(train, pd.DataFrame), "Train should be a DataFrame"
    assert isinstance(test, pd.DataFrame), "Test should be a DataFrame"
    assert isinstance(data, pd.DataFrame), "Data should be a DataFrame"


# TODO: implement the second test. Change the function name and input as needed
def test_train_test_shape():
    """
    # Unit test to check if the train/test shapes equal the shape of the data DataFrame
    
    """
    assert train.shape[0] + test.shape[0] == data.shape[0]


# TODO: implement the third test. Change the function name and input as needed
def test_train_test_size():
    """
    # Unit test to check if the train/test split is correct

    """
    assert train.shape[0] == math.floor(0.8 * data.shape[0])
    assert test.shape[0] == math.ceil(0.2 * data.shape[0])

def test_score_types():
    """
    # Unit test to check if the score types are correct
    """
    from ml.model import compute_model_metrics
    from sklearn.metrics import precision_score, recall_score, fbeta_score

    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert isinstance(precision, float), "Precision should be a float"
    assert isinstance(recall, float), "Recall should be a float"
    assert isinstance(fbeta, float), "F-beta score should be a float"
