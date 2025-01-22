from functionnal_api_test.functionnal_param import get_endpoint_base_url


class ApiUrls:
    Get_user="base_url"+"endpoints"
    @staticmethod
    def get_users():
        return get_endpoint_base_url() + "public/v2/users"
    @staticmethod
    def get_user_by_id(user_id):
        return get_endpoint_base_url() + f"public/v2/users/{user_id}"
    @staticmethod
    def post_users():
        return get_endpoint_base_url() + f"public/v2/users"
    @staticmethod
    def post_user_by_id(user_id):
        return get_endpoint_base_url() + f"public/v2/users/{user_id}"
