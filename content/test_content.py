import json
import pytest
from common import connect_api


class TestContent:
    @pytest.fixture
    def check_status(self):
        return connect_api.status() is True

    @pytest.mark.parametrize('user, password, version, text, expected', [
        ('alice', 'wonderland', 'v1', 'life is beautiful', True),
        ('alice', 'wonderland', 'v2', 'life is beautiful', True),
        ('alice', 'wonderland', 'v1', 'that sucks', False),
        ('alice', 'wonderland', 'v2', 'that sucks', False),
    ])
    def test_content_analysis(self, user, password, version, text, expected, check_status):
        """
        Test authorization
        """
        if not check_status:
            pytest.skip('API is not available')

        r = connect_api.sentiment(user, password, version, text)
        parsed = json.loads(r.content)
        sentiment = parsed['score']
        assert (sentiment > 0) == expected, f"Expected {expected}. Actual sentiment {sentiment}. Response text {r.content}"

