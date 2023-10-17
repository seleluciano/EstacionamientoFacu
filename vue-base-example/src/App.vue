<template>
  <div id="app">
    <RegistrarUsuario/>
    <InicioSesion/>
    <Estacionamiento/>
  </div>
</template>

<script>
/* eslint-disable */
import InicioSesion from './components/InicioSesion.vue';
import RegistrarUsuario from './components/RegistrarUsuario.vue';
import Estacionamiento from './components/Estacionamiento.vue'
export default {
  name: 'App',
  components: {
    RegistrarUsuario,
    InicioSesion,
    Estacionamiento
}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>