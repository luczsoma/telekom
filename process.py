from csv import reader, writer
from os import scandir
from os.path import join, isfile
from pathlib import Path


def main():
    for isp in ["telekom", "dravanet"]:
        isp_raw_dir_path = Path(join("raw", isp))
        isp_processed_dir_path = Path(join("processed", isp))

        if not isp_raw_dir_path.exists():
            print(f'raw logs for ISP "{isp}" not found')
            continue

        isp_raw_dir_path.mkdir(parents=True, exist_ok=True)
        input_files = [f for f in scandir(isp_raw_dir_path) if isfile(f)]
        for input_file in input_files:
            with open(input_file, "rt", encoding="utf-8") as input:
                csv_reader = reader(input)

                isp_processed_dir_path.mkdir(parents=True, exist_ok=True)
                with open(
                    join(isp_processed_dir_path, input_file.name),
                    "wt",
                    encoding="utf-8",
                ) as output_file:
                    csv_writer = writer(output_file, lineterminator="\n")
                    for row in csv_reader:
                        # remove header rows
                        if row[0] == "Mtr_Version":
                            continue

                        # remove mtr version from rows
                        row.pop(0)

                        csv_writer.writerow(row)


if __name__ == "__main__":
    main()
