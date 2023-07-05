import axios from 'axios';

const asignacion_usuario = (formData) => {
    const url_axios = 'https://sistemaasesback.onrender.com/asignacion/asignacion_usuario/';
    axios({
        url:  url_axios,
        method: "POST",
        data: formData,
        // {
        //     "llamada":"asignar",
        //     "id_jefe":"1",
        //     "id_usuario": "10"
        // }
    })
    .catch(err=>{
        console.log(err);
    })
}
  
export default {
    asignacion_usuario
}