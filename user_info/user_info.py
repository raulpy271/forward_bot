from json import load


class User_Info():
    def __init__(self):
        # json with your token
        user_info_directory = "user_info/.user_info.json" 
        self.user_info = self.__load_user_info(user_info_directory)


        self.token = self.user_info["token"]
        self.forwarding_list_of_all_users = self.user_info[
            "forwarding_list_of_all_users"]


    def __load_user_info (self, json_directory):
        with open(json_directory, "r") as user_info_json:
            return load(user_info_json)


user_info = User_Info()
token = user_info.token
forwarding_list_of_all_users = user_info.forwarding_list_of_all_users


