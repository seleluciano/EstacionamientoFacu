<template>
    <div>
        <h1>ESTACIONAMIENTO UTN</h1>
        <div class="columns">
            <div class="column">
                <h2>NUMERO</h2>
                <ul v-for="Sensor in sensores" :key="Sensor.id">
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
    background-color: bisque;
    width: 100%;
    height: 80%;
}

p,
h1,
ul,
h2 {
    color: black;
    font-family: cursive;
}

input {
    background-color: rgb(202, 208, 228);
}

.columns {
    display: flex;
    justify-content: space-between;
}

.column {
    flex: 1;
    margin-right: 10px;
}

button {
    color: white;
    font-family: cursive;
}

.Ocupado {
    background-color: red;
}

.Desocupado {
    background-color: green;
}
</style>