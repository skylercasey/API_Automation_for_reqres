import requests
from TestData import test_data
from Logs import log_file


class UserPageMethods:
    log=log_file.log_func()
    def check_list_of_user_api(self, page_number):
        flag=True
        try:
            self.log.info(f"Api is {test_data.user_page_get_list_user_url.format(page_number)}")
            r=requests.get(test_data.user_page_get_list_user_url.format(page_number))
            if r.status_code==200:
                self.log.info(f"status code of API is {r.status_code} ")
            else:
                self.log.error(f"expected status code is 200 but got {r.status_code}")
                flag=False
            if r.json()['page']==page_number:
                self.log.info("Response is correct")
                self.log.info(f"page number is {page_number} ")
            else:
                self.log.error("response is not Correct")
                self.log.error(f"expected page value is {page_number} but Actual page value is {r.json()['page']}")
                flag=False
        except Exception as e:
            self.log.error(f"Exception {e} occured")
            flag=False
        return flag
