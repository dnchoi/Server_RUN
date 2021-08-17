import glob
import os


def main():
    root_dir = "/home/kevin/Documents/projects/data/FDDB/fddb_openvino_unlabeled"
    files = glob.glob(os.path.join(root_dir, "*"))

    for i, file in enumerate(files, 1):
        name, ext = os.path.splitext(file)

        target_file = os.path.join(root_dir, f"{i:04}{ext}")

        os.rename(file, target_file)


if __name__ == "__main__":
    main()
