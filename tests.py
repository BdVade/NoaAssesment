import os
from subprocess import getstatusoutput, getoutput

prg = './compress.py'


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_runnable():
    """Runs using python3"""

    out = getoutput(f'python {prg} uncompressed_test compressed_test')
    with open("compressed_test", 'r') as file:
        compressed_string = "".join(file.read().split())
    assert compressed_string == "a3b3c3aa"
