import pyreadr
import glob, os


errors = []

for fn in glob.glob("*.rda"):
    try:
        data = pyreadr.read_r(fn, timezone="PST")
    except Exception as e:
        errors.append(fn)
        continue
    if not data:
        errors.append(fn)
        continue
    for df in data.values():
        if fn == "ncdc_normals.rda":
            df.to_csv(
                os.path.join(
                    os.path.dirname(__file__),
                    f"../csv_files/{fn.split('.')[-2]}.csv.zip",
                ),
                index=False,
                compression="zip",
            )
        else:
            df.to_csv(
                os.path.join(
                    os.path.dirname(__file__),
                    f"../csv_files/{fn.split('.')[-2]}.csv",
                ),
                index=False,
            )
if len(errors) > 0:
    with open(os.path.join(os.path.dirname(__file__), "../errors.txt"), "w") as f:
        f.writelines([f"{e}\n" for e in errors])
