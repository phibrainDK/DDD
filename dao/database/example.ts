// DI : Depe
interface UsuarioService{
    findOne(id:string, a:number):string ;
    save(data:any):void
}
class UsuarioServiceImplFa implements UsuarioService{
    findOne(id: string, a: number): string {
        throw new Error("Method not implemented.");
    }
    save(data: any): void {
        throw new Error("Method not implemented.");
    }
}
class UsuarioServiceImplFb implements UsuarioService{
    findOne(id: string, a: number): string {
        throw new Error("Method not implemented.");
    }
    save(data: any): void {
        throw new Error("Method not implemented.");
    }
}
class Consumidor {
    constructor(
        // DI  ('UsuarioServiceImplFb' , 'UsuarioServiceImpla')
        private usuarioService: UsuarioService
    ){
    }
    casdsad(){
        this.usuarioService.findOne
    }
}
