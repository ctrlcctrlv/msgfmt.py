"""Tests msgfmt against GNU bash's ja.po"""
import os
from io import BytesIO
from pathlib import Path
from tempfile import mkstemp

import pytest
from fixtures import *

from msgfmt import make


def test_bash(script_loc, tmp_path):
    pon = tmp_path / "ja.po"
    mon = tmp_path / "ja.mo"

    with open(script_loc.joinpath(Path("data") / "ja.mo"), "rb") as f:
        mo = f.read()
    with open(script_loc.joinpath(Path("data") / "ja.po"), "rb") as f:
        with open(pon, "wb+") as f2:
            f2.write(f.read())

    make(str(pon), str(mon))

    with open(mon, "rb") as mo2:
        assert mo2.read() == mo
