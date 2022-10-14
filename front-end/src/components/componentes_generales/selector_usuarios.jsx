import React, {useState} from 'react';
import  {useEffect} from 'react';
import axios from 'axios';
import Select from 'react-select'  ;
import Switch from 'react-switch'
import {Container, Row, Col, Dropdown, Button, Modal, ModalHeader, ModalBody} from "react-bootstrap";
import Form from 'react-bootstrap/Form';
import all_user_service from '../../service/all_users'
import Accordion from 'react-bootstrap/Accordion';
import Table from 'react-bootstrap/Table';
import DataTable, {createTheme} from 'react-data-table-component';
const selector_usuarios = () =>{

  /*
    constantes
  */
  const datos_option_user = []
  const datos_option_rol = []
  var bandera_consulta_rol = true;
  var bandera_consulta_user_rol = true;
  var bandera_option_user = true;
  var bandera_option_rol = true;

  const [state,set_state] = useState({
    rol: '',
    rol_actual: '',
    usuario : '',
    id_rol: '',
    id_usuario : '',
    data_user : [],
    data_user_rol : [],
    data_rol : [],
    info_modal : " cargando...",
  })
  const [show, setShow] = useState(false);
  const columnas =[
    {
      name: 'USERNAME',
      selector: row => row.username
    },
    {
      name: 'NOMBRES',
      selector: row => row.first_name
    },
    {
      name: 'APELLIDOS',
      selector: row => row.last_name
    },
    {
      name: 'EMAIL',
      selector: row => row.email
    },
    {
      name: 'ROL',
      selector: row => row.nombre
    },
  ]
  /*
    UseEffect: se ejecuta al iniciar la pestaña. En el está alojada la función de traer todos los usuarios
    necesaria para el selector de usuarios.
  */
  useEffect(()=>{
    axios({
      // Endpoint to send files
      url:  "http://127.0.0.1:8000/usuario_rol/alluser/",
      method: "GET",
    })
    .then((respuesta)=>{
      set_state({
        ...state,
        data_user : respuesta.data
      })
    })
    .catch(err=>{
        return (err)
    })
    
  },[]);
  /*
    UseEffect: se ejecuta al iniciar la pestaña. En el está alojada la función de traer todos los usuarios
    necesaria para el selector de usuarios.
  */
  const consulta_all_rol = (e)=>{
    if(bandera_consulta_rol==true){
      axios({
        // Endpoint to send files
        url:  "http://127.0.0.1:8000/usuario_rol/allrol/",
        method: "GET",
      })
      .then((respuesta)=>{
        set_state({
          ...state,
          data_rol : respuesta.data
        })
      })
      .catch(err=>{
          return (err)
      })
      bandera_consulta_rol = false;
      console.log(bandera_consulta_rol)

    }

    
  }
  const consulta_all_user_rol = (e)=>{
    if(bandera_consulta_user_rol==true){
      axios({
        // Endpoint to send files
        url:  "http://127.0.0.1:8000/usuario_rol/all_user_rol/",
        method: "GET",
      })
      .then((respuesta)=>{
        set_state({
          ...state,
          data_user_rol : respuesta.data
        })
      })
      .catch(err=>{
          return (err)
      })

      bandera_consulta_user_rol = false;
      console.log(bandera_consulta_user_rol)

    }
  }

  const handle_user_selector = (e) => {

    if(bandera_option_user==true){
      for (var i = 0; i < state.data_user['length'] ; i++) {
        const dato = { value: state.data_user[i]['first_name']+" "+state.data_user[i]['last_name'], label: state.data_user[i]['first_name']+" "+state.data_user[i]['last_name'],id:state.data_user[i]['id'] }
        datos_option_user.push(dato)
      }
      console.log([datos_option_user]);
      bandera_option_user = false;
    }
    else{
      console.log([datos_option_user]);
    }
  }

  const handle_rol_selector = (e)=>{
    if(bandera_option_rol==true){

      for (var i = 0; i < state.data_rol['length'] ; i++) {
        const dato2 = { value: state.data_rol[i]['nombre'], label: state.data_rol[i]['nombre'],id:state.data_rol[i]['id'] }
        datos_option_rol.push(dato2)
      }
      console.log([datos_option_rol]);
      bandera_option_rol = false;
    }
    else{
      console.log([datos_option_rol]);
    }
  }
  

 


  const handle_option_user = (e) => {
    // Getting the files from the input
    console.log(e)
    let formData = new FormData();
  
    //Adding files to the formdata
    formData.append('id', e.id);
    axios({
      // Endpoint to send files
      url:  "http://127.0.0.1:8000/usuario_rol/user_rol_manage/",
      method: "POST",
      data: formData,
    })
    .then(res=>{set_state({
      ...state,
      usuario : [e.value],
      id_usuario : [e.id],
      rol_actual: res.data
      
    })})
    .catch(err=>{
      set_state({
        ...state,
        usuario : [e.value],
        id_usuario : [e.id],
        rol_actual: "" 
      })}
    )
    console.log(state.usuario)
    console.log(state.rol_actual)

  }
  const handle_option_rol = (e) => {
    console.log(e)
    set_state({
      ...state,
      rol : [e.value],
      id_rol : [e.id],
    })
  }

  const handle_upload = (e) => {
    // Getting the files from the input
    console.log([state.id_rol[0]])
    console.log([state.id_usuario[0]])
    let formData = new FormData();
  
    //Adding files to the formdata
    formData.append('id_rol', state.id_rol[0]);
    formData.append('id_user', state.id_usuario[0]);
    axios({
      // Endpoint to send files
      url:  "http://127.0.0.1:8000/usuario_rol/user_rol/",
      method: "POST",
      data: formData,
    })
    .then(res=>{set_state({
      ...state,
      info_modal: "El rol se asignó correctamente"
      
    })})
    .catch(err=>{
      set_state({
        ...state,
        info_modal: "ocurrio un error"
    })})
    setShow(true);
  }
  const set_info = (e) => {
    bandera_option_user = true;
    bandera_option_rol = true;
    bandera_consulta_rol = true;
    setShow(false)
    set_state({
      ...state,
      rol: '',
      rol_actual: '',
      usuario : '',
      id_rol: '',
      id_usuario : '',
      info_modal : "cargando..",
    })
    axios({
      // Endpoint to send files
      url:  "http://127.0.0.1:8000/usuario_rol/allrol/",
      method: "GET",
    })
    .then((respuesta)=>{
      set_state({
        ...state,
        data_rol : respuesta.data
      })
    })
    .catch(err=>{
        return (err)
    })

  }
  const handleClose = () => setShow(false);
  return (
        <Container>
        <Accordion>
          <Accordion.Item onMenuOpen={consulta_all_rol} eventKey="0">
            <Accordion.Header >Selector de Usuarios</Accordion.Header>
            <Accordion.Body>
            <Row className="g-2">
                <h3>Selecciona un usuario</h3>
            </Row>
            <Row className="mb-3">

                <Select class="form-control" options={datos_option_user} onMenuOpen={handle_user_selector} onChange={handle_option_user} className="justMargin1" />
                
            </Row>
            <Row className="g-2">
                <h6>Nombre Completo:</h6>
            </Row>
            <Row className="g-2">
                <Form.Control as="textarea" value={state.usuario}  rows={1} readOnly/>
            </Row>
            <Row className="g-2">
                <h6>Rol actual:</h6>
            </Row>
            <Row className="g-2">
                <Form.Control as="textarea" value={state.rol_actual}  rows={1} readOnly/>
            </Row>
            <Row className="g-2">
                <h3>Selecciona un Rol</h3>
            </Row>

            <Row className="g-2" >
              <Select class="form-control"  options={datos_option_rol} onMenuOpen={handle_rol_selector} onChange={handle_option_rol} className="justMargin1" />
                
            </Row>
            <Row className='mt-2'> 
                <Col lg={{ span: 1, offset: 5}}>
                    <Button onClick={handle_upload}>Aceptar</Button> 
   
                </Col>
                <Col>

                    <Button onClick={set_info}>Cancelar</Button> 
                </Col>    
            </Row>
            </Accordion.Body>
          </Accordion.Item>
          <Accordion.Item  onChange={consulta_all_user_rol} eventKey="1">
          <Accordion.Header >Lista de Usuarios</Accordion.Header>
            <Accordion.Body>
              <DataTable 
              columns={columnas}
              data={state.data_user_rol}
              pagination
              />
            </Accordion.Body>
          </Accordion.Item>

        </Accordion>
        <Modal show={show} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>ESTADO ASIGNACIÓN</Modal.Title>
          </Modal.Header>
          <Modal.Body>{state.info_modal}</Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={set_info}>
              OK
            </Button>
          </Modal.Footer>
        </Modal>
            
        </Container>
  )
}

export default selector_usuarios


  
  
  
