import json


class User_Info():
    def __init__(self):
        self.user_info = self.__load_user_info("user_info.json")
        self.is_restrict = self.user_info["restrict_for_only_admins"] 
        self.token = self.user_info["token"]
        if self.is_restrict:
            self.admins = self.user_info["admins"]
            self.admins_id = self.__make_admins_id_list()


    def __load_user_info (self, json_directory):
        with open(json_directory, "r") as user_info_json:
            return json.load(user_info_json)


    def __make_admins_id_list (self):
        admins_dic = self.admins
        admins_id = list( 
            map( ( lambda admins : int(admins["user_id"]) ), admins_dic))
        return admins_id


    def get_admins_id(self):
        return self.admins_id


    def add_admins_id(self, user_id):
        self.admins_id.append(user_id)

