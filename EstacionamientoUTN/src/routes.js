import Estacionamiento from './components/Estacionamiento.vue'
import RegistrarUsuario from './components/RegistrarUsuario.vue'
import InicioSesion from './components/InicioSesion.vue'
import iniciopagina from './components/iniciopagina.vue'
/* eslint-disable */
const routes = [
   {
    path: '/registro',
    component: RegistrarUsuario
  },
  {
    path: '/inicio',
    component: InicioSesion
  },
  {
    path: '/estacionamiento',
    component: Estacionamiento
  },
  {
    path: '/',
    component: iniciopagina
  }
]
export default routes