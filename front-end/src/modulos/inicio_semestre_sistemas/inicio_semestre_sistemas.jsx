import React, {useState} from 'react';
import Semestre__sistemas_component from "../../components/inicio_semestre_sistemas/semestre_sistemas_component"
import {Container, Row} from "react-bootstrap";

const Inicio_semestre_sistemas = () =>{

    return (
        <Container>
            <Row className="rowJustFlex">
                <h1>INICIO DE SEMESTRE - SISTEMAS</h1>
            </Row>
            <Row className="containerRow">
                <Semestre__sistemas_component/>
            </Row>
        </Container>
    )
}

export default Inicio_semestre_sistemas