# Data

The `rda` files from the book's data [repository](https://github.com/clauswilke/dviz.supp/tree/master/data) were converted to `.csv` files and saved in `csv_files/`.

To obtain the data files from the [repository](https://github.com/clauswilke/dviz.supp/tree/master/data), navigate to your desired directory in a PowerShell command line and execute the following command:

    $url = "https://api.github.com/repos/clauswilke/dviz.supp/contents/data"
    $response = Invoke-RestMethod -Uri $url

    foreach ($file in $response) {
        $downloadUrl = $file.download_url
        $filename = Split-Path $file.path -Leaf
        Invoke-WebRequest -Uri $downloadUrl -OutFile $filename
    }


To convert the files to `.csv` format, run:

    python convert_to_csv.py

There are currently 11 files that have errors that are not converted. They are listed in `errors.txt`.
