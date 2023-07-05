import axios from 'axios';

const all_users_rols = async () => {
    try {
        const url_axios = 'https://sistemaasesback.onrender.com/usuario_rol/usuario_rol/';
        const resUserRol = await axios(url_axios)
        return resUserRol.data;
        
    } catch (error) {
        console.log(error);
    }
}

export default{
    all_users_rols
}