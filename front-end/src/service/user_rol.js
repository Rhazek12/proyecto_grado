import axios from 'axios';

const user_rol = (formData) => {
    const url_axios = 'https://sistemaasesback.onrender.com/usuario_rol/usuario_rol/';
    axios({
        url:  url_axios,
        method: "POST",
        data: formData,
    })
    .catch(err=>{
        console.log(err);
    })
}
  
export default {
    user_rol
}