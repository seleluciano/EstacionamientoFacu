<template>
    <div>
        <h1>ESTACIONAMIENTO UTN</h1>
        <div class="columns">
            <div class="column">
                <h2>NUMERO</h2>
                <ul v-for="Sensor in sensores" :key="Sensor.id" class="ID">
                    <li>{{ Sensor.id }}</li>
                </ul>
            </div>
            <div class="column">
                <h2>ESTADO</h2>
                <ul v-for="Sensor in sensores" :key="Sensor.id">
                    <button v-if="Sensor.estado == true" class="Ocupado">Ocupado</button>
                    <button v-if="Sensor.estado == false" class="Desocupado">Desocupado</button>
                </ul>
            </div>
        </div>
    </div>
</template>
<script>
/* eslint-disable */
import axios from 'axios'

export default {
    name: 'APITest',
    data: function () {
        return {
            sensores: [],
            estado: ''
        }
    },
    mounted() {
        axios.get('http://localhost:8000/sensores/')
            .then(response => {
                this.sensores = response.data;
            })
            .catch(error => {
                console.error(error);
            })
    }
}
</script>
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: #f4f4f4; /* Un tono más suave que bisque */
    font-family: Arial, sans-serif; /* Cambiado a una fuente más común */
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

p,
h2 {
    color: black;
    font-family: cursive;
}

.container {
    background-color: #fff;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    text-align: center;
}

h1 {
    font-family: 'Helvetica Neue', sans-serif;
    color: #333;
    margin-bottom: 20px;
}

.columns {
    display: flex;
    justify-content: space-between;
}

.column {
    flex: 1;
    margin-right: 10px;
}
.ID {
    color: black;
    font-family: 'Helvetica Neue', sans-serif;
    border: none;
    border-radius: 4px;
    padding: 12px 20px;
    margin-top: 8px; /* Ajuste para que estén a la misma altura */
    cursor: pointer;
}
button {
    color: white;
    font-family: 'Helvetica Neue', sans-serif;
    background-color: #007BFF;
    border: none;
    border-radius: 4px;
    padding: 12px 20px;
    margin-top: 10px; /* Ajuste para que estén a la misma altura */
    cursor: pointer;
}
input {
    background-color:rgb(167, 167, 233);
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    margin: 10px 0;
    width: 100%;
}

a {
    color: #007BFF;
    text-decoration: none;
    margin: 10px 0;
    display: inline-block;
}

.Ocupado {
    background-color: red;
}

.Desocupado {
    background-color: green;
}

/* Elimina los márgenes y el relleno en las listas */
ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

/* Permite que el texto se desborde fuera de la lista */
li {
    overflow: visible;
}

</style>