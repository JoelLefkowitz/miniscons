from src.containers import flatten, merge_maps, unique


def test_unique():
    assert unique(["a", "b", "b"]) == ["a", "b"]


def test_flatten():
    assert flatten(["a", ["b", "c"]]) == ["a", "b", "c"]


def test_merge_maps():
    assert merge_maps({}, {}, ["a"]) == {"a": []}
    assert merge_maps({"a": [1]}, {"a": [2, 3]}, ["a"]) == {"a": [1, 2, 3]}
