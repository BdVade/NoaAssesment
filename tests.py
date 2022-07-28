import os
from subprocess import getstatusoutput, getoutput

prg = './compress.py'


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_runnable():
    """Runs correctly"""

    out = getoutput(f'python {prg} uncompressed_test compressed_test')
    with open("compressed_test", 'r') as file:
        compressed_string = "".join(file.read().split())
    assert compressed_string == "12312s;dfklasdlqwejkasdS3a270"
