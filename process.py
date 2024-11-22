from argparse import ArgumentParser
from csv import reader, writer
from os import scandir
from os.path import join, isfile


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("isp", choices=["telekom", "dravanet"])
    args = parser.parse_args()
    isp = args.isp

    input_files = [f for f in scandir(join("raw", isp)) if isfile(f)]
    for input_file in input_files:
        with open(input_file, "rt", encoding="utf-8") as input:
            csv_reader = reader(input)

            with open(
                join("processed", isp, input_file.name), "wt", encoding="utf-8"
            ) as output_file:
                csv_writer = writer(output_file, lineterminator="\n")
                for row in csv_reader:
                    if row[0] == "Mtr_Version":
                        # header row
                        continue

                    # remove mtr version
                    row.pop(0)

                    csv_writer.writerow(row)


if __name__ == "__main__":
    main()
