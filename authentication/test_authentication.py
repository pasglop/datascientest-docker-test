import pytest

from common import connect_api


class TestAuthentication:
    @pytest.fixture
    def check_status(self):
        return connect_api.status() is True

    def assert_status(self, response, status=200):  # you can assert other status codes too
        assert response.status_code == status, \
            f"Expected {status}. Actual status {response.status_code}. Response text {response.text}"

    @pytest.mark.parametrize('user, password', [
        ('alice', 'wonderland'),
        ('bob', 'builder'),
    ])
    def test_authenticate_success(self, user, password, check_status):
        """
        Test authentication
        Checking authentication for users
        """
        if not check_status:
            pytest.skip('API is not available')

        self.assert_status(connect_api.authenticate(user, password))

    @pytest.mark.parametrize('user, password', [
        ('alice', 'clementine'),
        ('bob', 'mandarine'),
    ])
    def test_authenticate_fail(self, user, password, check_status):
        if not check_status:
            pytest.skip('API is not available')

        self.assert_status(connect_api.authenticate(user, password), status=403)
