import subprocess
import sys
import pathlib
import os

def main():
    p = pathlib.Path(sys.argv[1])
    subprocess.call(['jupytext', '--to', 'py', str(p)])
    py_file = p.parent / pathlib.Path(p.stem + '.py')
    subprocess.call(['autoflake',
                     '--in-place',
                     '--remove-unused-variables',
                     '--remove-duplicate-keys',
                     '--remove-all-unused-imports',
                     '--expand-star-imports', str(py_file)])

    subprocess.call(['autopep8', '--in-place', str(py_file)])
    subprocess.call(['importanize', str(py_file)])
    subprocess.call(['jupytext', '--to', 'notebook', str(py_file)])
    print("cleaning up")
    os.remove(py_file)


if __name__ == '__main__':
    main()
