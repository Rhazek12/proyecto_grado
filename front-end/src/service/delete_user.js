import axios from 'axios';

const delete_user_rol = (id_usuario) => {
    try {
        const url_axios = 'https://sistemaasesback.onrender.com/usuario_rol/user/' + id_usuario + '/';
        const url_usuario_rol = 'https://sistemaasesback.onrender.com/usuario_rol/usuario_rol/' + id_usuario + '/';

        axios({
            url:  url_axios,
            method: "DELETE",
        })
        .catch(err=>{
            console.log(err);
        })
    } catch (error) {
        console.log(error);
    }
}
  
export default {
    delete_user_rol
}