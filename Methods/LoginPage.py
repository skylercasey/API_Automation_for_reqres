import requests
from TestData import test_data
from Logs import log_file

class LoginPage:

    log=log_file.log_func()
    def check_login_api_with_valid_cred(self):
        flag=True
        try:
            r = requests.post("https://reqres.in/api/login", data=test_data.valid_credentials)
            status_code=r.status_code
            self.log.info(f"status code is {status_code}")
            if status_code!=200:
                self.log.error("ststus code is not 200")
                flag=False
            else:
                self.log.info("correct status code")
            if not r.json()["token"]:
                self.log.error("Token is not present")
                flag=False
            else:
                self.log.error("Token is present")
        except Exception as e:
            self.log.error(f"exception occured {e}")
            flag=False
        return flag

    def check_login_api_with_invalid_cred(self):
        flag=True
        r = requests.post("https://reqres.in/api/login", data=test_data.invalid_credentials)
        status_code=r.status_code
        if status_code!=200:
            flag=False
        return flag

