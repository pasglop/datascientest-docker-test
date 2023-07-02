import pytest

from common import connect_api


class TestAuthorization:
    @pytest.fixture
    def check_status(self):
        return connect_api.status() is True

    def assert_status(self, response, status=200):  # you can assert other status codes too
        assert response.status_code == status, \
            f"Expected {status}. Actual status {response.status_code}. Response text {response.text}"

    @pytest.mark.parametrize('user, password, version', [
        ('alice', 'wonderland', 'v1'),
        ('alice', 'wonderland', 'v2'),
        ('bob', 'builder', 'v1'),
    ])
    def test_authorized_success(self, user, password, version, check_status):
        """
        Test authorization
        """
        if not check_status:
            pytest.skip('API is not available')

        self.assert_status(connect_api.authorize(user, password, version))

    @pytest.mark.parametrize('user, password, version', [
        ('bob', 'mandarine', 'v2'),
    ])
    def test_authorized_fail(self, user, password, version, check_status):
        if not check_status:
            pytest.skip('API is not available')

        self.assert_status(connect_api.authorize(user, password, version), status=403)
