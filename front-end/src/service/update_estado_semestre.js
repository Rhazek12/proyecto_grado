import axios from 'axios';

const update_estado = async (semestre_id) => {
    try {
      const url_axios = 'http://localhost:8000/wizard/semestre/' + semestre_id.toString()+"/";
      const resUserRol = await axios(url_axios)
      return resUserRol.data;
      
    } catch (error) {
        console.log(error);
    }
  }
  
export default {
    update_estado
}