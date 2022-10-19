import React, {useState} from 'react';
import {Container, Row, Col, Dropdown} from "react-bootstrap";
import Info_general from "./tabs/info_general"
import Academico from "./tabs/academico"
import {Tab, Tabs, TabList, TabPanel} from 'react-tabs';
import DropdownItem from 'react-bootstrap/esm/DropdownItem';
import {FaRegChartBar, FaThList, FaBars} from "react-icons/fa";
import { NavLink } from 'react-router-dom';

const Selector = (props) =>{

    const[switchChecked, setChecked] = useState(false);
    const handleChange = () => setChecked(!switchChecked);


    const datos_option_user = []
    const datos_option_rol = []
    var bandera_option_user = true;
    var bandera_option_rol = true;
    var bandera = true;
    const [state,set_state] = useState({
      usuario : '',
      data_user : [],
      data_rol : [],

      id_usuario:'',
      nombres:'',
      apellidos: '',
      cedula:'',
      correo:'',
      telefono:'',

    })

/*
    useEffect (() => {
        // Getting the files from the input
        console.log(e)
        let formData = new FormData();
      
        //Adding files to the formdata
        formData.append('id', e.id);
        axios({
          // Endpoint to send files
          url:  "http://127.0.0.1:8000/usuario_rol/estudiante_manage/",
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
    
      },[]);
*/



    const[activeTabIndex, setActiveTabIndex] = useState(0);
    const activeTab = (index)=> 
    {
        index === activeTabIndex ?
        (setActiveTabIndex(0))
        :
        setActiveTabIndex(index)
    }


    const tabs=[
        {
            id:1,
            name:"General",
            contnido:"2siiiiiii",
            component:<Info_general id={props.id} seleccionado={props.seleccionado} editar={props.editar}/>,
        },
        {
            id:2,
            name:"Socieducativo",
            contnido:"hola",
            component:<Info_general />,
        },
        {
            id:3,
            name:"Academico",
            contnido:"hola",

            component:<Academico />,
        },
        {
            id:4,
            name:"Geografico",
            contnido:"hola",
            component:<Info_general />,
        }
    ]



    return (
        <Container className="containerSelector">

                {Object.keys(tabs).length === 0 ? (
                    <Row>no tabs</Row>
                ) : (
                        <Row className="tabs" >
                            {tabs.map((tab, index)=>(
                                <Row className={tab.id === activeTabIndex ? "tab_separador" : "tab"} >
                                    <Row onClick={() => activeTab(tab.id)}>
                                        <label key={index} className={tab.id === activeTabIndex ? "activeTab" : "tab"}>
                                            {tab.name}{props.editar}
                                        </label>
                                    </Row>
                                    
                                    {
                                        (tab.id === activeTabIndex)?
                                        (
                                        
                                        <Row>
                                            <Col xs={"0"} md={"1"}></Col>
                                            <Col className="contentTab" xs={"12"} md={"10"}>{tabs[activeTabIndex-1].component}</Col>
                                            <Col xs={"0"} md={"1"}></Col>

                                        </Row>)
                                        :
                                        (<Row></Row>)
                                    }
                                
                                </Row>
                                
                                ))
                            }
                        </Row>

                )}
                
        </Container>
    )
}

export default Selector 