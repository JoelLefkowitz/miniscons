from src.environment import inherit


def test_inherit():
    assert "PATH" in inherit()
