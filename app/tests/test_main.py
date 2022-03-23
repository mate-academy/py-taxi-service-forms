import pytest

from ..main import main


@pytest.mark.django_db
def test_main():
    users = main()
    assert list(users.values_list("name")) == [
        ("Dan",),
        ("Robert",),
    ]
