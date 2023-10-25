<template>
  <div id="app">
    <router-link to="/RegistrarUsuario">Registrar Usuario</router-link>
    <router-link to="/InicioSesion">Iniciar Sesion</router-link>
    <router-link to="/">Estacionamiento</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
/* eslint-disable */ 
export default {
  name: 'App'
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