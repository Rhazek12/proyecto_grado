import { useEffect, useState } from 'react';
import { Container, Row, Col, Dropdown, Button, Modal, ModalHeader, ModalBody, FormCheck } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import '../../Scss/campus_diverso/campus_diverso.css';
import axios from 'axios';

const Registro_estudiante = () => {
  const [estado, setEstado] = useState({
    id_pertenencia_grupo_poblacional: '',
   
  });
  const [state, set_state] = useState({
    correo: "",
    nombre_identitario: "",
    nombre_y_apellido: "",
    tipo_documento: "",
    estrato_socioeconomico: "",
    ciudad_nacimiento: "",
    fecha_nacimiento: "",
    municipio_nacimiento: "",
    departamento_nacimiento: "",
    pais_nacimiento: "",
    ciudad_residencia:"",
    zona_residencia:"",
    direccion_residencia:"",
    barrio_residencia:"",
    comuna_barrio:"",
    telefono:"",
    estado_civil:"",
    identidad_etnico_racial:"",
    nombre_persona_confianza:"",
    telefono_persona_confianza:"",


  });

  const [razasOptions, setRazasOptions] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Realizar una solicitud GET al servidor para obtener las opciones de raza
    axios.get(`${process.env.REACT_APP_API_URL}/campus_diverso/pertenencia_grupo_poblacional/`)
      .then((response) => {
        const opciones = response.data.map((id_pertenencia_grupo_poblacional) => id_pertenencia_grupo_poblacional.nombre_grupo_poblacional);
        setRazasOptions(opciones); // Suponiendo que el servidor devuelve una lista de opciones
        setIsLoading(false);
      })
      .catch((error) => {
        console.error('Error al obtener las opciones de raza:', error);
        setIsLoading(false);
      });
  }, []);

  const handleChange = (e) => {
    set_state({
      ...state,
      ...estado,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Aquí puedes enviar una solicitud POST a la base de datos utilizando Axios



    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/campus_diverso/persona/`, state);
      console.log('Respuesta del servidor:', response.data);
    } catch (error) {
      console.error('Error al enviar la solicitud:', error);
    }
  };

  return (
    <>
    <Container className="container_informacion_general" xs={"10"} sm={"6"}>
      <Col xs={"10"} md={"5"}>
       

        <div>
          <label>nombre identitario</label>
          <div>
            <input
              type="text"
              placeholder="Enter username"
              name="nombre_identitario"
              value={state.nombre_identitario}
              onChange={handleChange}
            />
          </div>
        </div>

        <div>
          <label>nombre y apellido</label>
          <div>
            <input
              className='input'
              type="text"
              placeholder="Ingrese nombre y apellido"
              name="nombre_y_apellido"
              value={state.nombre_y_apellido}
              onChange={handleChange}
            />
          </div>
        </div>
       
   
        <div>
          <label>Tipo de documento</label>
          <div>
            <input
              className='input'
              type="text"
              placeholder="123456"
              name="tipo_documento"
              value={state.tipo_documento}
              onChange={handleChange}
            />
          </div>
        </div>
        
        <div>
          <label>Estrato socioeconomico</label>
          <div>
            <input
              type="number"
              placeholder="Estrato"
              name="estrato_socioeconomico"
              value={state.estrato_socioeconomico}
              onChange={handleChange}
              pattern='[0-9]*'
            />
          </div>
        </div>
       
      </Col>

      
      
      <Col md={"6"}>
    
      <div>
          <label>Ciudad de nacimiento</label>
          <div>
            <input
              type="text"
              placeholder="Ingrese ciudad de nacimiento"
              name="ciudad_nacimiento"
              value={state.ciudad_nacimiento}
              onChange={handleChange}
              pattern='[0-9]*'
            />
          </div>
        </div>

        <div>
          <label>Fecha de nacimiento</label>
          <div>
            <input
              type="date"
              name="fecha_nacimiento"
              value={state.fecha_nacimiento}
              onChange={handleChange}
            />
          </div>
        </div>

        <div>
          <label>Grupo poblacional</label>
          <div>
            {isLoading ? (
              <p>Cargando...</p>
            ):(
            <select
              name="id_pertenencia_grupo_poblacional"
              value={state.id_pertenencia_grupo_poblacional}
              onChange={handleChange}
              
              
            >
              <option value="">Seleccione un grupo poblacional </option>
              {razasOptions.map((id_pertenencia_grupo_poblacional, index) => (
                <option key={index} value={id_pertenencia_grupo_poblacional}>
                  {id_pertenencia_grupo_poblacional} 
                </option>
              ))}
              
              </select>
              )}
          </div>
        </div>

        <div>
          <label>Municipio de nacimiento</label>
          <div>
            <input
              type="text"
              placeholder="Ingrese el municipio"
              name="municipio_nacimiento"
              value={state.municipio_nacimiento}
              onChange={handleChange}

            />
          </div>
        </div>

        <div>
          <label>Departamento de nacimiento</label>
          <div>
            <input
              type="text" 
              placeholder="Ingrese el departamento"
              name="departamento_nacimiento"
              value={state.departamento_nacimiento}
              onChange={handleChange}

            />
          </div>
        </div>

        <div>
          <label>País de nacimiento</label>
          <div>
            <input
              type="text" 
              placeholder="Ingrese el departamento"
              name="pais_nacimiento"
              value={state.pais_nacimiento}
              onChange={handleChange}

            />
          </div>
        </div>

        <div>
          <label>Ciudad de residencia</label>
          <div>
            <input
              type="text" 
              placeholder="Ingrese el departamento"
              name="ciudad_residencia"
              value={state.ciudad_residencia}
              onChange={handleChange}

            />
          </div>
        </div>

        <div>
          <label>Zona de residencia</label>
          <div>
            <input
              type="text" 
              placeholder="Ingrese el departamento"
              name="zona_residencia"
              value={state.zona_residencia}
              onChange={handleChange}

            />
          </div>
        </div>

        <div>
          <label>Direccion de residencia</label>
          <div>
            <input
              type="text" 
              placeholder="Ingrese su direccion"
              name="direccion_residencia"
              value={state.direccion_residencia}
              onChange={handleChange}

            />
          </div>
        </div>
        
        <div>
          <label>Barrio de residencia</label>
          <div>
            <input
              type="text" 
              placeholder="Ingrese su barrio"
              name="barrio_residencia"
              value={state.barrio_residencia}
              onChange={handleChange}

            />
          </div>
        </div>
        
      </Col>
      

    </Container>
          <Row >
          <Col  className="text-center">
            <button type="submit" className= "btn btn-danger" onClick={handleSubmit}>Enviar</button>
          </Col>
        </Row>
        </>
    
  );
}

export default Registro_estudiante;
