from src.containers import flatten, unique


def test_unique():
    assert unique(["a", "b", "b"]) == ["a", "b"]


def test_flatten():
    assert flatten(["a", ["b", "c"]]) == ["a", "b", "c"]
