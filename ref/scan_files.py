from os import scandir


def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for dir_or_file in scandir(path):
        if dir_or_file.is_dir(follow_symlinks=False):
            yield from scantree(dir_or_file.path)  # see below for Python 2.x
        else:
            yield dir_or_file


if __name__ == '__main__':
    import sys
    for dir_or_file in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):
        print(dir_or_file.path)
