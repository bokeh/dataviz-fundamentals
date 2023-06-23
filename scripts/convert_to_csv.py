import pyreadr
from pathlib import Path


errors = []
need_zip = [
    "ncdc_normals.rda",
]

rda_dir = Path("../data/rda_files")
csv_dir = Path("../data/csv_files")
errors_file = Path("..") / "data" / "errors.txt"

for fn in rda_dir.glob("*.rda"):
    base_name = fn.name
    try:
        data = pyreadr.read_r(str(fn), timezone="PST")
    except Exception as e:
        errors.append(base_name)
        continue
    if not data:
        errors.append(base_name)
        continue
    for df in data.values():
        if base_name in need_zip:
            csv_file = csv_dir / f"{base_name.removesuffix('.rda')}.csv.zip"
            zip_kw = dict(compression="zip")
        else:
            csv_file = csv_dir / f"{base_name.removesuffix('.rda')}.csv"
            zip_kw = dict()
        df.to_csv(csv_file, index=False, **zip_kw)

if len(errors) > 0:
    with open(errors_file, "w") as f:
        f.writelines([f"{e}\n" for e in errors])
