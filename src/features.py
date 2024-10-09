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


feature_name = [
    "approval_status" "loan_id",
    "business_id",
    "dismissal_description",
    "sector",
    "principal",
    "total_owing_at_issue",
    "application_number",
    "applying_for_loan_number",
    "loan_number",
    "paid_late",
    "total_recovered_on_time",
    "total_recovered_15_dpd",
    "cash_yield_15_dpd",
]


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

    logger.success("Features generation complete.")
    data.to_csv(output_path, columns=feature_name, index=False)


if __name__ == "__main__":
    main()
