from pathlib import Path

from category_encoders import OrdinalEncoder
from dotenv import load_dotenv

from src.utils import get_logger

# logging.
logger = get_logger("Config")

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Categorical features configuration.
unique_dismissal_dict = {
    "none:approved loan.": 1,
    "Client does not have all of the requirements": 2,
    "Client travelling away from business": 3,
    "declined": 4,
    "Unable to contact client": 5,
    "application expired": 6,
    "Client does not have ID": 7,
    "application cancelled.": 8,
    "Expired": 9,
    "Trading license is fake": 10,
    "Client does not have business": 11,
    "Client no longer interested": 12,
    "Client blacklisted from Numida": 13,
    "Client thought that loan amount was too small": 14,
    "Client has just started new business (<6 months)": 15,
    "Client is not owner of business": 16,
    "Fraudulent Transactions": 17,
    "Concentration risk in same shop": 18,
    "Client does not have multiple loan requirements": 19,
    "Client has active Numida loan on different number": 20,
    "Client got money elsewhere": 21,
    "Client will reapply when loan limit increases": 22,
    "Client was testing loan feature": 23,
    "Business revenues too low to finance": 24,
    "Someone used client's phone to apply for loan": 25,
    "Client thought requirements were too onerous": 26,
    "Loan purpose is not for business use": 27,
    "Client does not have mobile money account in their name": 28,
    "Client does not have smartphone to enter transactions consistently": 29,
    "Client did not trust Numida and refused to submit personal data": 30,
    "Client will reapply after upgrading to new version": 31,
    "Client in blacklisted industry (i.e. metalwork, woodwork, agriculture,hawker)": 32,
    "Industry blacklisted due to Coronavirus impact": 33,
    "Client will reapply after updating transactions in app": 34,
}
dismissal_encoder = OrdinalEncoder(
    cols=["dismissal_description"],
    mapping=[{"col": "dismissal_description", "mapping": unique_dismissal_dict}],
)
unique_sector_dict = {
    "Beauty Fashion": 1,
    "Food Staple Goods": 2,
    "Metal and Woodworking": 3,
    "Mobile Money Airtime": 4,
    "Hospitality": 5,
    "School": 6,
    "Phones Electronics": 7,
    "Manufacturing": 8,
    "Stationary Printing": 9,
    "Autoparts Hardware": 10,
    "Other": 11,
    "Repairs Cleaning": 12,
    "Drugshop": 13,
    "Arts Media": 14,
    "Agro Input": 15,
    "Wholesale": 16,
    "Transportation": 17,
    "Health Clinic": 18,
    "Advisory Consultants": 19,
}
sector_encoder = OrdinalEncoder(
    cols=["sector"], mapping=[{"col": "sector", "mapping": unique_sector_dict}]
)
approval_encoder = OrdinalEncoder(
    cols=["approval_status"],
    mapping=[
        {
            "col": "approval_status",
            "mapping": {"Approved": 1, "Declined": 2, "Cancelled": 3, "Expired": 4},
        }
    ],
)


# try:
#     from tqdm import tqdm

#     logger.remove(0)
#     logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
# except ModuleNotFoundError:
#     pass
