import click
import pandas as pd

from src.utils import get_logger

# logging.
logger = get_logger("Datasets")


# Replace missing values with "none" in column: 'dismissal_description'
# if the appoval status is apporved.
def missing_dismissal(df):
    if df["approval_status"] == "Approved":
        return "none:approved loan."
    if df["approval_status"] == "Declined":
        return "declined"
    if df["approval_status"] == "Cancelled":
        return "application cancelled."
    if df["approval_status"] == "Expired":
        return "application expired"


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def main(
    input_path,
    output_path,
):
    logger.info("Processing dataset...")
    data = pd.read_csv(input_path)

    # Missing Values.
    data["dismissal_description"] = data["dismissal_description"].fillna(
        data.apply(missing_dismissal, axis=1)
    )
    data = data.fillna({"total_owing_at_issue": 0})
    data = data.fillna({"total_recovered_on_time": 0})
    data = data.fillna({"total_recovered_15_dpd": 0})
    data = data.fillna({"cash_yield_15_dpd": 0})
    data = data.fillna({"loan_number": 0})

    # Drop Duplicates.
    data = data.drop_duplicates()

    data.to_csv(output_path, index=False)

    logger.info("Processing dataset complete.")


if __name__ == "__main__":
    main()
