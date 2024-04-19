from src.containers import flatten


def test_flatten():
    assert flatten(["a", ["b", "c"]]) == ["a", "b", "c"]
