
from warnings import catch_warnings

import pytest
import requests

class FrameworkUtils:
    @staticmethod
    def fire_api_request(request_method=None,request_url=None,request_params=None,request_json=None,headers=None,expected_status_code=None):

        response = requests.request(request_method,request_url,params=request_params,headers=headers,json=request_json)
        print(response.json())
        try:
            assert response.status_code ==expected_status_code ,\
                f"API call failed ,expected status code is {expected_status_code}but found is {response.status_code}"
            return response
        except :
            pytest.fail(f"API call failed ,expected status code is {expected_status_code} but found is {response.status_code}")
