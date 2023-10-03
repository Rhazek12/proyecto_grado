import axios from 'axios';

const url = `${process.env.REACT_APP_API_URL}/validate`

const verificar_token = async () => {
    try {
        const config = {
            headers: {
                Authorization: 'Bearer ' + sessionStorage.getItem('token')
            }
        };
        const token = {
            "token": sessionStorage.getItem('token')
        }
        const url_axios = `${process.env.REACT_APP_API_URL}/validate`;
        const resInst = await axios.post(url_axios, token, config)
        if('Tienes un token activo' === resInst.data['message']){
            return true
        } else {
            return false
        }
    } catch (error) {
        return false
    }
  }

  export default {
    verificar_token
}