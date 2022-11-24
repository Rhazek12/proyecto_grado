import React, {useState} from 'react';
import Select from 'react-select'  ;
import Switch from 'react-switch'
import {Container, Row, Col, Dropdown, Button} from "react-bootstrap";
import {FaRegChartBar, FaThList, FaBars} from "react-icons/fa";
import {DropdownItem, DropdownToggle, DropdownMenu} from 'reactstrap';
import { NavLink } from 'react-router-dom';
import Desplegable from "./desplegable";

/*
Tabla Conteo de Seguimientos:
- codigo
- Nombres
- Apellidos
- documento
- Conteos
--- Fichas normales
--- Fichas de inasistencias
----Total conteos
- Profesional
- Practicante
- Monitor
*/



const Informacion_rol = () =>{
    return (
        <Container className="container_reportes_seguimientos">

            <Row className="row_contenido_reportes_seguimientos">
                <Col className="row_card_reportes_seguimientos">
                    <Row className="row_card_content_flex">
                        <Col className="subrow_card_content_flex" xs={"12"} sm={"6"}>
                            <Row>
                                Informacion: Rol
                            </Row>
                            <p className="subrow_card_content_flex">Fichas:      Revisado : 0    No revisado : 1     Total : 1</p>
                            <Row>Inasistencias: Revisado : 0    No revisado : 0     Total : 0</Row>
                        </Col>
                        <Col className="subrow_card_content_flex" xs={"12"} sm={"6"}>
                            <Row>Practicante</Row>
                            <Row>Fichas: Revisado : 0 - No revisado : 1 - Total : 1</Row>
                            <Row>Inasistencias: Revisado : 0 - No revisado : 0 - Total : 0</Row>
                        </Col>
                    </Row>
                </Col>
            </Row>

            <Row className="row_contenido_reportes_seguimientos">
                        <Col className="subrow_card_content_flex" xs={"12"} sm={"6"}>
                            <Row>
                                <Col  xs={"6"} md={"3"}>
                                Informacion:
                                </Col>
                                <Col xs={"6"} md={"3"}>
                                Rol
                                </Col>
                            </Row>
                            <Row>
                                <Col xs={"6"} md={"3"}>
                                Fichas:
                                </Col>
                                <Col xs={"6"} md={"3"}>
                                Revisado : 0
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                No revisado : 1
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                Total : 1
                                </Col>
                                               
                            </Row>
                            <Row>
                                <Col xs={"6"} md={"3"}>
                                Inasistencias:
                                </Col>
                                <Col xs={"6"} md={"3"}>
                                Revisado : 0
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                No revisado : 0
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                Total : 0
                                </Col>          
                            </Row>
                        </Col>
                        <Col className="subrow_card_content_flex" xs={"12"} sm={"6"}>
                            <Row>
                                <Col xs={"6"} md={"3"}>
                                Practicante:
                                </Col>
                                <Col xs={"6"} md={"3"}>
                                nombre
                                </Col>
                            </Row>
                            <Row>
                                <Col xs={"6"} md={"3"}>
                                Fichas:
                                </Col>
                                <Col xs={"6"} md={"3"}>
                                Revisado : 0
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                No revisado : 1
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                Total : 1
                                </Col>
                                               
                            </Row>
                            <Row>
                            <Col xs={"6"} md={"3"}>
                                Inasistencias:
                                </Col>
                                <Col xs={"6"} md={"3"}>
                                Revisado : 0
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                No revisado : 0
                                </Col>
                                <div class="d-block d-md-none col-6"></div>
                                <Col xs={"6"} md={"3"}>
                                Total : 0
                                </Col>           
                            </Row>
                        </Col>

            </Row>
                <Desplegable></Desplegable>
        </Container>
    )
}

export default Informacion_rol 



