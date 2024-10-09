import pickle

import click
import pandas as pd

from src.utils import get_logger

# from pathlib import Path
# from src.config import MODELS_DIR

# logging.
logger = get_logger("Predict")


# url: Path = MODELS_DIR / "rf_model.pkl"
url = "model/rf_model.pk"
model = pickle.load(open(url, "rb"))


def prediction(df):
    pred = model.predict(df)
    return pred[0]


def predict_probability(df):
    pred_proba = model.predict_proba(df)
    return round(pred_proba[0].max() * 100, 2)


@click.command()
@click.argument("predictions_path", type=click.Path(exists=True))
def main(
    predictions_path,
):
    """
    main

    Predict and give prediction probability.

    Parameters
    ----------
    predictions_path :
        path of file with preprocessed data ready for prediction.

    Returns
    -------
    Dataframe:
        dataframe for a dataset that has more than one row.
    Str:
        text explaining results of prediction.

    """

    logger.info("Performing inference for model...")
    data = pd.read_csv(predictions_path)

    if data.shape[0] == 1:
        approval = prediction(data)
        proba = predict_probability(data)

        if approval == 0:
            return f"The loan applied is Approved, the prediction percentage is {proba}%"
        if approval == 2:
            return f"The loan applied is Declined, the prediction percentage is {proba}%"
        if approval == 3:
            return f"The loan applied is Cancelled, the prediction percentage is {proba}%"
        if approval == 4:
            return f"The loan applied is Expired:, the prediction percentage is {proba}%"

    else:
        temp = data.columns
        batch_predicitons = model.predict(temp)
        proba_df = pd.DataFrame(
            model.predict_proba(temp),
            columns=[
                "Approved",
                "Declined",
                "Cancelled",
                "Expired",
            ],
        )
        data["Prediction"] = batch_predicitons
        data["Prediction"] = data["Prediction"].map(
            {0: "Approved", 1: "Declined", 2: "Cancelled", 3: "Expired"}
        )
        comb_df = pd.concat([data, proba_df], axis=1)
        return comb_df

    logger.info("Inference complete.")


if __name__ == "__main__":
    main()
