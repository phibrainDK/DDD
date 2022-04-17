# from dependency_injector import containers, providers
# from dependency_injector.wiring import Provide, inject
# from dao.database.commands import CreateUser, EditStatusUser, EditUser, GetUsers
# from dao.database.controllers import (
#     get_users_from_db,
#     create_user_from_db,
#     update_user_from_db,
# )


# class UpdateUser:
#     edit_status_user: EditStatusUser
#     edit_user: EditUser


# class UserController:
#     update_user_from_db: UpdateUser
#     create_user_from_db: CreateUser
#     get_users_from_db: GetUsers


# class UserService:


#     def get_filter_users(self, cmd: GetUsers):
#         return create_user_from_db(cmd)

#     def create_user_db(self, cmd: CreateUser):
#         return create_user_from_db(cmd)

#     def update_user_db(self, cmd: )

# class UserContainer(containers.DeclarativeContainer):
