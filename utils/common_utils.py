import  random


class Common_utilities:
    @staticmethod
    def get_custom_headers():
        header={
            "Accept":"application/json",
            "content-type":"application/json",
            "Authorization":"d8df4fbd4fafe80e3ea4b2f4fece43bd2c14ecdb28d1f851e45f19b4d5fc0fa3"
        }
        return header


    def get_unique_email():
        random_no=random.randint(1000,99000)
        email=f"test_automation{random_no}@gmail.com"
        return email