# from typing import Any
# from uuid import UUID
# class UsuarioServiceImplFa:
#     def findOne(id: UUID, a : int) -> str:
#         return str(id) + str(a)

#     def save(data: Any) -> None:
#         return data


# class UsuarioServiceImplFb:
#     def findOne(id: UUID, a : int) -> str:
#         return str(id) + str(id)  + str(a) + "fregrege"

#     def save(data: Any) -> None:
#         pass


# class Person{
#     handleEdit(cmd: EditPerson){
#         if(this.status==='ACTIVO'){
#             throw {}
#         }
#         this.
#     }
# }


# class PersonService{
#     constructor (private personDao:any ){
#     }
#     editPerson(cmd: any /*EditPerson */){
#         const persona=   this.personDao.findById(cmd.id);
#         if persona.gregre = cmd.grepigre

#         persona.handleEdit(cmd);
#         persona.save();
#         this.personDao.save(persona);
#     }
# }

# class PersonController{
#     @Inject()
#     personService: PersonService
#     @Post()
#     save ( @Body cmd: EditPerson){
#         personService.editPerson(cmd)
#     }
# }
