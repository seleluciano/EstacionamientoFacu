import Estacionamiento from './components/Estacionamiento.vue'
import RegistrarUsuario from './components/RegistrarUsuario.vue'
import InicioSesion from './components/InicioSesion.vue'
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
    path: '/',
    component: Estacionamiento
  }
]
export default routes