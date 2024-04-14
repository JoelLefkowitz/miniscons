from src.services.compiler import compiler
from src.services.environment import inherit


def test_compiler():
    assert compiler("c++11", ["all"], ["deprecated-declarations"]) == [
        "-std=c++11",
        "-Wall",
        "-Wno-deprecated-declarations",
    ]


def test_environment():
    assert "PATH" in inherit()
