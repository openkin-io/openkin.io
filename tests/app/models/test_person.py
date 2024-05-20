import pytest

pytestmark = pytest.mark.django._db

class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory(name="test-post")
        assert post.__str__() == "test-post"
