from src.build import Build
from src.routine import Routine
from src.script import Script
from src.target import Target
from src.tasks import Tasks
from textwrap import dedent


def test_cli():
    main = Build("main", ["main.cpp"])
    start = Target("start", main)

    cppcheck = Script("cppcheck", [["main.cpp"], "--enable=all"])
    lint = Routine("lint", [cppcheck])

    tasks = Tasks([main], [start], [cppcheck], [lint])
    assert tasks.cli == dedent(
        """
        builds:
          main

        targets:
          start -> main

        scripts:
          cppcheck

        routines:
          lint -> [cppcheck]

        flags:
          -
        """
    )
