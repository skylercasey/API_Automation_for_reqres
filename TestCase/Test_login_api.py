import pytest
import requests
from Methods.LoginPage import LoginPage


class TestLogin(LoginPage):
    @pytest.mark.pappu
    def test_login_api_with_correct_cred(self):
        flag=self.check_login_api_with_valid_cred()
        assert flag is True


    def test_login_api_with_incorrect_pass(self):
        flag=self.check_login_api_with_invalid_cred()
        assert flag is True