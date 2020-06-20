import os

def add_suffix_to_file_path(path: str, suffix: str) -> str:
    dirname = os.path.dirname(path)
    basename = os.path.basename(path)
    filename, ext = basename.split('.')

    return os.path.join(dirname, "%s-%s.%s" % (filename, suffix, ext))

def wc_l(path: str) -> int:
    # count total lines in a file
    s = 0
    with open(path, "r") as f:
        for _ in f:
            s += 1
    return s