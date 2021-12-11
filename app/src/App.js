import './App.css';
import {useState, useEffect} from 'react'
import axios from 'axios'
import './Tarjetas.css'
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';
import Divider from '@mui/material/Divider';
import Chip from '@mui/material/Chip';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';


function App() {

  const [query,setQuery] = useState('')
  const [persona,setPersona] = useState([])
  const [mascota,setMascota] = useState([])

  
  

  useEffect(() => {
    if (!query) return

    axios.get(`http://localhost:5000/persona/${query}`).then(res => {
      let resultado = res.data
      setPersona(resultado.items.map(item => {
        let mascot = item[0].mascotas
        setMascota(mascot.map(item => {
          return {
            id: item.id_mascota, 
            nombre: item.nombre,
            imagen: item.imagen
          }


        }))
        
        
        console.log(item[0].nombre)
        return {
          id: query, 
          nombre: item[0].nombre,
          apellido: item[0].apellido,
          imagen: item[0].imagen
        }
      }))
    })


  }, [query])

  console.log(mascota)

  return (
    <div className="App">
      <Box component="form" sx={{ '& > :not(style)': { m: 1, width: '25ch' },}} noValidate autoComplete="off">
      <TextField id="outlined-name" label="ID de la persona" value={query} onChange={e => setQuery(e.target.value)} />
      </Box>
      <div className="cards_container">
        {persona.map(p => (
          <div>
            <Avatar alt={p.nombre} src={p.imagen} sx={{ width: 500, height: 500 }}/>
            <h1>{p.nombre} {p.apellido}</h1>
            <Divider>
              <Chip label="MASCOTAS" />
            </Divider>
            <br></br>
            <Stack direction="row" spacing={2}>
            { mascota.map(m => (
              <div>
                <Avatar alt = {m.nombre} src = {m.imagen} sx={{ width: 150, height: 150 }}/>
              <p size="medium">{m.nombre}</p>
              </div>
              

             ))}
             </Stack>
          </div>

        ))}
      </div>
    </div>
  );
}


export default App;
