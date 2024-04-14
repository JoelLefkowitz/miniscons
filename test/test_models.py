from textwrap import dedent
from src.models.tasks import Tasks
from src.models.builds.build import Build


def test_targets():
    assert str(Tasks([Build("main", [])])) == dedent(
        """
        builds:
          main

        targets:
          -

        scripts:
          -

        routines:
          -

        flags:
          -
        """
    )
