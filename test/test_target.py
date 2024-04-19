from src.build import Build
from src.target import Target


def test_action():
    test = Target("test", Build("tests"), ["--gtest_brief"])
    assert test.action == "dist/tests --gtest_brief"
