from pathlib import Path

from pytest import fixture


@fixture(scope="module")
def script_loc(request):
    """Return the directory of the currently running test script"""
    return Path(request.fspath).parent
