from src.script import Script


def test_action():
    lint = Script(
        "lint", ["clang-tidy", ["main.cpp", "feature.cpp"], "--", "-I/includes"]
    )
    assert lint.action == "clang-tidy main.cpp feature.cpp -- -I/includes"
