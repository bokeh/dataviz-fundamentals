import pyreadr
from pathlib import Path
import sys


ERRORS = []
NEEDS_ZIP = ("ncdc_normals.rda",)

rda_dir = Path("../data/rda_files")
csv_dir = Path("../data/csv_files")
errors_file = Path("..") / "data" / "errors.txt"

for fn in rda_dir.glob("*.rda"):
    base_name = fn.name
    try:
        data = pyreadr.read_r(str(fn))
    except Exception as e:
        print(f"Exception error in '{base_name}': {e}", file=sys.stderr)
        continue
    if not data:
        print(f"Empty data in '{base_name}'", file=sys.stderr)
        continue
    for df in data.values():
        if base_name in NEEDS_ZIP:
            csv_file = csv_dir / f"{base_name.removesuffix('.rda')}.csv.zip"
            zip_kw = dict(compression="zip")
        else:
            csv_file = csv_dir / f"{base_name.removesuffix('.rda')}.csv"
            zip_kw = dict()
        df.to_csv(csv_file, index=False, **zip_kw)
