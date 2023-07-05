import axios from 'axios';

const url = "https://sistemaasesback.onrender.com/login"

const login = (info) => {
    axios.post("https://sistemaasesback.onrender.com/login", {
      'username' : info.username,
      'password' : info.password
    })
    .then(res=>{
      console.log(res.data)
      sessionStorage.setItem('token', res.data.token)
      sessionStorage.setItem('user', res.data.user.nombre_completo)
      sessionStorage.setItem('refresh-token', res.data['refresh-token'])
    })
    .catch(err=>console.log(err))
  }

  export default {
    login
}