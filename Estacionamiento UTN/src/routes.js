import Estacionamiento from './components/Estacionamiento.vue'
import RegistrarUsuario from './components/RegistrarUsuario.vue'
import InicioSesion from './components/InicioSesion.vue'
/* eslint-disable */
const routes = [
   {
    path: '/RegistrarUsuario',
    component: RegistrarUsuario
  },
  {
    path: '/InicioSesion',
    component: InicioSesion
  },
  {
    path: '/',
    component: Estacionamiento
  }
]
export default routes