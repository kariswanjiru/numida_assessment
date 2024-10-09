from pathlib import Path

import click

from src.config import FIGURES_DIR
from src.utils import get_logger

# logging.
logger = get_logger("Make plots")


@click.command()
@click.argument("prepocessed_path", type=click.Path(exists=True))
def main(
    input_path,
    output_path: Path = FIGURES_DIR / "plot.png",
):
    logger.info("Generating plot from data...")
    # ---- REPLACE THIS WITH YOUR OWN CODE ----

    logger.info("Plot generation complete.")


if __name__ == "__main__":
    main()
