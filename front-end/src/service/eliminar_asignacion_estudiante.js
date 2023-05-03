import axios from 'axios';

const eliminar_asignacion = async (id_estudiante) => {
    try {
      const url_axios = 'http://localhost:8000/asignacion/asignacion_estudiante' + id_estudiante.toString()+"/";
      const resUserRol = await axios(url_axios)
      return resUserRol.data;
      
    } catch (error) {
        console.log(error);
    }
  }
  
export default {
    eliminar_asignacion
}