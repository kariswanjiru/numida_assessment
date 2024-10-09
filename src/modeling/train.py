# loading libraries and packages
import pickle

import click
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score, recall_score

from src.utils import get_logger

# from pathlib import Path
# from src.config import MODELS_DIR

# logging.
logger = get_logger("Train Machine Learning Model")


@click.command()
@click.argument("prepocessed_path", type=click.Path(exists=True))
@click.argument("test_preprocessed_path", type=click.Path(exists=True))
def main(
    prepocessed_path,
    test_preprocessed_path,
    # TODO: add to function. model_path: Path = MODELS_DIR / "rf_model.pkl",
):
    logger.info("Training some model...")
    loan = pd.read_csv(prepocessed_path)

    test = pd.read_csv(test_preprocessed_path)

    # Data targets
    features = loan.drop("approval_status", axis=1)
    target = loan["approval_status"]

    # Test target
    test_features = test.drop("approval_status", axis=1)
    test_target = test["approval_status"]

    # Update the random forest classifier
    rf_model = RandomForestClassifier()
    rf_model.fit(features, target)
    prediction = rf_model.predict(test_features)

    # Measure Metrics
    logger.info(balanced_accuracy_score(prediction, test_target))
    logger.info(recall_score(prediction, test_target, average="micro"))

    # Outputting model.
    model_path = "model/rf_model.pkl"
    pickle.dump(rf_model, open(model_path, "wb"))

    logger.info("Modeling training complete.")


if __name__ == "__main__":
    main()
