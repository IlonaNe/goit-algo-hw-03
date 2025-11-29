from pathlib import Path
import argparse

def copy_file(source: Path, destination: Path):
    """Copies a file """
    with open(source, "rb") as f_src:
        with open(destination, "wb") as f_dest:
          f_dest.write(f_src.read())
     


def sort_copied_files(source: Path, destination: Path):
    """
    Recursively goes through all files and folders in 'source'.
    Copies each file into 'destination' sorted by extension.
    """
    for item in source.iterdir():
        if item.is_dir():
            sort_copied_files(item, destination)

        else:
            file_extension = item.suffix.lower().replace(".", "")
            if file_extension == "":
                file_extension = "no_extension"

            # Create destination folder: dist/txt/
            target_folder = destination / file_extension
            target_folder.mkdir(parents=True, exist_ok=True)

            # Path where the file will be copied
            new_file_path = target_folder / item.name

            # Copy file
            try:
                copy_file(item, new_file_path)
                print(f"Copied: {item} → {new_file_path}")
            except Exception as e:
                print(f"Error copying {item}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Sort and copy files by extension."
    )

    parser.add_argument("source", type=Path, help="Path to source folder")
    parser.add_argument("destination", type=Path, help="Path to destination folder")

    args = parser.parse_args()

    if not args.source.exists():
        print(f"Error: source folder '{args.source}' does not exist.")
        return

    args.destination.mkdir(parents=True, exist_ok=True)

    sort_copied_files(args.source, args.destination)
    print("Done!")


if __name__ == "__main__":
    main()