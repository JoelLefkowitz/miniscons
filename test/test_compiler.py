from src.compiler import flags


def test_flags():
    assert flags("c++11", ["error"], ["shadow"]) == [
        "-std=c++11",
        "-Werror",
        "-Wno-shadow",
    ]
