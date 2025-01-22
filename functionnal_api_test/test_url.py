

import functionnal_api_test.functionnal_param
from config.api_config import ApiUrls
from req_resp.requests.gorest import Gorest
from utils.common_utils import Common_utilities
from utils.framework_utils import FrameworkUtils


def test_url():
    # url=functionnal_api_test.functionnal_param.get_endpoint_base_url()
    # print("url :",url)
    get_url=ApiUrls.get_users()
    post_users_url=ApiUrls.post_users()
    # print(post_users_url)
    # post_user_by_id_url = ApiUrls.post_user_by_id(123456)
    # print(post_user_by_id_url)
    # get_user_by_id_url=ApiUrls.get_user_by_id(123456)
    # print(post_users_url)
    # print(get_user_by_id_url)
    # print("testing headers ")
    header_body=Common_utilities.get_custom_headers()
    # print("headers",header_body)
    # email=Common_utilities.get_unique_email()
    # print("email :",email)
    create_user = Gorest.CREATE_USER
    # print("CREATE_USER",CREATE_USER)
    # response = FrameworkUtils.fire_api_request(request_method='get', request_url=get_url,
    #                                           headers=header_body, expected_status_code=200)
    # print(response.json())
    response=FrameworkUtils.fire_api_request(request_method="PATCH",request_url= get_url,headers=header_body,request_json=create_user,expected_status_code=200)
    print(response.json())



test_url()