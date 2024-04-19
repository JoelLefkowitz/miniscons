from src.build import Build
from src.compiler import flags


def test_target():
    tests = Build("tests", ["test.cpp"])
    assert tests.target == "dist/tests"

    tests = Build("tests", ["test.cpp"], output="build")
    assert tests.target == "build/tests"
