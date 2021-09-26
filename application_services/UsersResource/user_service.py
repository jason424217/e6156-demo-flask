from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class UserResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    # TODO This can go into the base class.
    @classmethod
    def get_by_template(cls, template):
        res = d_service.RDBService.find_by_template("userresource", "users",
                                       template, None)
        return res