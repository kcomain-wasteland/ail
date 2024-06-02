import json
from pathlib import Path

DATADIR = (Path(__file__) / "../../data/").resolve()
SOURCE = DATADIR / "semiraw"
FINAL = DATADIR / "processed"


def convert_entries(entry: dict):
    data = ""
    for key, value in entry.items():
        data += f"{key.title()}: {value}\n"

    return data.strip()


if __name__ == "__main__":
    for file in list(SOURCE.glob("*.json")):
        new_data = []
        filename = file.stem
        print(f"Processing file {filename}")
        with file.open() as f:
            data = json.load(f).get("products")
            for count, datum in enumerate(data):
                print(f"\tProcessing datum {count}")
                new_data.append(convert_entries(datum))

        print(f"{len(new_data)} entries in new data")
        print(f"writing to destination")
        with (FINAL / (filename + ".txt")).open("w+") as f:
            b = f.write("\n\n--\n".join(new_data))
            print(f"Wrote {b} bytes.")
