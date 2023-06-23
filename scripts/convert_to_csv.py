import pyreadr
import glob, os


errors = []

for fn in glob.glob("../data/rda_files/*.rda"):
    try:
        data = pyreadr.read_r(fn, timezone="PST")
    except Exception as e:
        errors.append(os.path.basename(fn))
        continue
    if not data:
        errors.append(os.path.basename(fn))
        continue
    for df in data.values():
        if os.path.basename(fn) == "ncdc_normals.rda":
            df.to_csv(
                os.path.join(
                    "..",
                    "data",
                    "csv_files",
                    f"{os.path.splitext(os.path.basename(fn))[0]}.csv.zip",
                ),
                index=False,
                compression="zip",
            )
        else:
            df.to_csv(
                os.path.join(
                    "..",
                    "data",
                    "csv_files",
                    f"{os.path.splitext(os.path.basename(fn))[0]}.csv",
                ),
                index=False,
            )
if len(errors) > 0:
    with open(os.path.join("..", "data", "errors.txt"), "w") as f:
        f.writelines([f"{e}\n" for e in errors])
