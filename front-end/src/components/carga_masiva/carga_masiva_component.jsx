import React, {useState} from 'react';
import axios from 'axios';
import Select from 'react-select'  ;
import Switch from 'react-switch'
import {Container, Row, Col, Dropdown, Button} from "react-bootstrap";
import Form from 'react-bootstrap/Form';
import carga_masiva_service from '../../service/carga_masiva';
const carga_masiva_component = () =>{

  const[switchChecked, setChecked] = useState(false);
  

  const [state,set_state] = useState({
    file: null,
    option : '',
  })
  const handle_file = (e) => {
    // Getting the files from the input
    console.log(e.target.files[0])
    set_state({
      ...state,
      [e.target.name] : [e.target.files[0]],
    })
  }
  const handle_options = (e) => {
    // Getting the files from the input
    console.log(e.target.value)
    set_state({
      ...state,
      [e.target.name] : [e.target.value]
    })
  }
  const handle_upload=(e)=> {
    let file = [state.file];
    let option = [state.option];

    carga_masiva_service.carga_masiva(file,option);
  }

  return (
        <Container>

            <Row className="rowJustFlex">
                <h1>CARGA MASIVA</h1>
            </Row>

            <Row className="rowJustFlex">
                <Form.Select name= "option" onChange={handle_options} >
                  <option value="Estudiante">Estudiante</option>
                  <option value="Usuarios">Usuarios</option>
                  <option value="Materias">Materias</option>
                  <option value="Notas">Notas</option>
                  <option value="Resolución">Resolución</option>
                  <option value="Programa">Programa</option>
                  <option value="Retiros">Retiros</option>
                </Form.Select>
            </Row>

            <Row className="rowJustFlex">
                <Form.Control type="file" name='file' onChange={handle_file}/>      
            </Row>
            <Row className="rowJustFlex">
                <Button onClick={handle_upload}>Subir</Button>  
            </Row>
        </Container>
  )
}

export default carga_masiva_component


  
  
  