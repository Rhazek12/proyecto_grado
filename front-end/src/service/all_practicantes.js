import axios from 'axios';

const all_practicantes = async () => {
    try {
        const url_axios = 'https://sistemaasesback.onrender.com/usuario_rol/practicante/';
        const res = await axios.get(url_axios 
        //     {
        //         headers: {
        //         Authorization: 'Bearer ' + sessionStorage.getItem('token')
        //         }
        //    }
        )
        return res.data;
        
    } catch (error) {
    //     const resRol = {'data': 'error'}
    //     return(resRol.data);
        console.log(error);
    }
}

export default{
    all_practicantes
}