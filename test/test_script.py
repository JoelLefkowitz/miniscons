from src.script import Script


def test_action():
    clang_format = Script("clang-format", ["-i", ["main.cpp", "main.hpp"]])
    assert clang_format.action == "clang-format -i main.cpp main.hpp"

    cspell = Script("cspell", [".", "--dot"], ["npx"])
    assert cspell.action == "npx cspell . --dot"
