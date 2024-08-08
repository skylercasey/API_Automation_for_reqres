import pytest
from Methods.UserPage import UserPageMethods


class TestUserPage(UserPageMethods):

    @pytest.mark.parametrize("page_number",[2,10, 21,88,600])
    @pytest.mark.UserPage
    def test_get_user_list(self,page_number):
        self.parameterize_param=page_number
        status=self.check_list_of_user_api(page_number)
        assert status
