<template>
  <div id="app">
    <router-link to="/" style="margin-right: 20px;">Inicio</router-link>
    <router-link to="/registro" style="margin-right: 20px;">Registrar Usuario</router-link>
    <router-link to="/inicio" style="margin-right: 20px;">Iniciar Sesion</router-link>
    <!--<router-link to="/estacionamiento" style="margin-right: 20px;">Estacionamiento</router-link>-->
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
  font-family: Arial, sans-serif; /* Fuente más común y legible */
  background-color: #f4f4f4; /* Fondo ligeramente más claro */
  color: #333; /* Color de texto más oscuro para una mejor legibilidad */
  margin: 60px auto; /* Centrar la aplicación en la página */
  max-width: 100000px; /* Ancho máximo para el contenido */
  padding: 20px; /* Añadir espacio alrededor del contenido */
  border-radius: 8px; /* Agregar bordes redondeados */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave */
  text-align: center;
}
@media only screen and (min-width: 320px) {
  .grid {
      grid-template-columns: repeat(1, 100%);
      grid-template-rows: repeat(5, 20%);
  }
}
@media only screen and (min-width: 480px) {
  .grid {
      grid-template-columns: repeat(2, 50%);
      grid-template-rows: repeat(3, 33%);
  }
}
@media only screen and (min-width: 768px) {
  .grid {
      grid-template-columns: repeat(3, 34%);
      grid-template-rows: repeat(2, 50%);
  }
}
</style>