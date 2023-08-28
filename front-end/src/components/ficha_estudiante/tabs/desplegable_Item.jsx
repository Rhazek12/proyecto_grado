import React from 'react';
import {useState } from "react";
import {Container, Row, Col, Dropdown, Button} from "react-bootstrap";
import {FaRegChartBar, FaThList, FaGraduationCap, FaUser} from "react-icons/fa";
import Modal from 'react-bootstrap/Modal';
import Seguimiento_individual from '../../seguimiento_forms/form_seguimiento_individual_sin_boton';
import Seguimiento_inasistencia from '../../seguimiento_forms/form_inasistencia';

const Desplegable_item = ({item}) => {

    const [open, setOpen] = useState(false)

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const [show2, setShow2] = useState(false);
    const handleClose2 = () => setShow2(false);
    const handleShow2 = () => setShow2(true);

    const userRole = sessionStorage.getItem('rol');

    if(item.nombre){
        return (
            <>{ userRole === 'vcd_academico' || userRole === 'DIR_PROGRAMA' || userRole === 'DIRECTOR_ACADEMICO' ? <></> :
            <Row className="periodo_activo_o_no">
                        {item.Actual ? 
                        (<Col>El periodo se encuentra en curso</Col>)
                            :
                        (<Col>El periodo esta finalizado</Col>)}
            </Row>
            }</>
        )
    } else{
        return (
            <>{ userRole === 'vcd_academico' || userRole === 'DIR_PROGRAMA' || userRole === 'DIRECTOR_ACADEMICO' ? <></> :
            <Row>
            {/*<li >{JSON.stringify(item)}</li>*/}

                <Col className="col_reportes" >
                    <Row className="col_reportes_hover">
                    {
                        item.hora_inicio ?
                        (
                        <Col onClick={handleShow}>
                            Seguimeinto individual : {item.fecha}
                        </Col>
                        )
                        :
                        (
                        <Col onClick={handleShow2}>
                            Inasistencia : {item.fecha}
                        </Col>
                        )
                    }

                    </Row>
                </Col>
                
                <Seguimiento_inasistencia show={show2} onHide={handleClose2} handleClose={handleClose2} item={item} size="lg"/>

                <Seguimiento_individual show={show} onHide={handleClose} handleClose={handleClose} item={item} size="lg"/>
            </Row>
            }</>
        )
    }
    
    
}

export default Desplegable_item



