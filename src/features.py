import click
import pandas as pd

# data preprocessing
from src.config import approval_encoder, dismissal_encoder, sector_encoder
from src.utils import get_logger

# logging.
logger = get_logger("Features")


# Feature Engineering Function.
def feature_engineering(df):
    df.columns = df.columns.str.strip()

    # pre-processing risk levels to integers.
    df = approval_encoder.fit_transform(df)
    df = dismissal_encoder.fit_transform(df)
    df = sector_encoder.fit_transform(df)

    return df


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def main(
    input_path,
    output_path,
):
    logger.info("Generating features from dataset...")
    data = pd.read_csv(input_path)

    # Categorical Values.
    data = feature_engineering(data)

    # Binary Values.
    data["paid_late"] = data["paid_late"].replace({False: 0, True: 1})

    # Drop Columns.
    data = data.drop(
        columns=[
            "credit_officer_id",
            "acquisition_channel",
            "employee_count",
        ]
    )

    logger.success("Features generation complete.")
    data.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
