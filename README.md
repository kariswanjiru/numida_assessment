# numida_assessment

Take away assignment for Machine Learning Engineer.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Commands](#commands-to-use)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)


## Overview

### The challenge

This is the solution to the Numida assemement. The data file wasn't added to the repository. The dataset train_loan_data.csv, train_payment_data.csv and test_loan_data.csv are all added to the raw data folder as shown above.

### Commands
#### Steps to follow.
- raw_data: path to the raw data file stored data/raw folder. eg data/raw/train_loan_data.csv
- interim_processed_data: path to pre-preocessed stored in the data/interim folder. eg data/interim/train_loan_data.csv
- processed_data: path to pre-preocessed stored in the data/processed folder.
- processed_training_data: path of the training data on the processed data folder
- processed_test_data: path of the testing data on the preporocessing data.


1.Handle missing data and drop duplicates.Returns data frame with less missing data frame.
```code
 python src/dataset.py raw_data_path interim_processed_data_path
```
2.Handle categorical and boolean values in the dataset. Returns a dataframe with features used durinf training.
```code
 python src/features.py interim_processed_data processed_data_path
```
3.Train preprocesed data and validate using the testing data.
```code
 python src/modelling/train.py processed_training_data_path processed_test_data_path
```
4.Predict the using the model.
```code
 python src/modelling/predict.py processed_data_path
```




## My process

### Built with

- Pandas
- fast_ml
- catergory_encoder
- lazypredict
- click
- Skit-learn
- Matplotlib

### What I learned

I learnt how to use both .fillna and .apply to handle missing data points.

This is a code snippet of what i learnt, see below:

```python
# Replace missing values with approprite custom message in column: 'dismissal_description'.
def missing_dismissal(df):
    if df['approval_status']=='Approved':
        return "none:approved loan."
    if df['approval_status']=='Declined':
        return  "declined"
    if df['approval_status']=='Cancelled':
        return "application cancelled."
    if df['approval_status']=='Expired':
        return "application expired"

loan['dismissal_description'] = loan['dismissal_description'].fillna(loan.apply(missing_dismissal, axis=1))
test['dismissal_description'] = test['dismissal_description'].fillna(loan.apply(missing_dismissal, axis=1))
loan.head(5).style
```

### Continued development
Write code to make plots make plotting simpler using plot.py.


### Useful resources

- [Skit-learn](https://scikit-learn.org/stable/) - This helped me with deeper understanding of the use of skit-lern models.
- [Pandas](https://pandas.pydata.org/docs/) - Pandas docuentation.



## Author

- LinkedIn - [Wanjiru Kariuki](https://www.linkedin.com/in/wanjiru-kariuki/)
