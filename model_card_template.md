# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Model date: 06/13/2025
Model version: 1.0.0
Model type: Machine learning model using RandomForestClassifier as the training model

## Intended Use

The model is used to be able to predict the likelihood of any of the values of the any of the categories in the dataset are to occur.

## Training Data

80% of the data from census.csv obtained from the U.S. Census Bureau

## Evaluation Data

20% of the data from census.csv obtained from the U.S. Census Bureau

## Metrics

Precision: 0.7444 | Recall: 0.6397 | F1: 0.6881

## Ethical Considerations

There are really no ethical considerations considering this dataset is already publicly available for anyone to us, plus there is no personally identifiable information about anyone in said dataset.

## Caveats and Recommendations

If additional data is included in the dataset in the future, the model should be retrained and retested to maintain effectiveness.