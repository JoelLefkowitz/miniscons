from src.services.compiler import compiler


def test_compiler():
    assert compiler(
        "c++11",
        ["all"],
        ["deprecated-declarations"],
    ) == [
        "-std=c++11",
        "-Wall",
        "-Wno-deprecated-declarations",
    ]
