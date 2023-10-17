<template>
    <div>
        <h1>ESTACIONAMIENTO</h1>
        <ul>
            <li>Id</li>
            <li>Estado</li>
            <ul v-for="Sensor in sensores" :key="Sensor.id">
                <li>{{ Sensor.id }}</li>
                <li>{{ Sensor.estado }}</li>
            </ul>
        </ul>
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
        axios.get('http://localhost:8080/')
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
    background-color: rgb(31, 49, 209);
    width: 100%;
    height: 80%;
}

p,
h1,
ul {
    color: black;
    font-family: cursive;
}

input {
    background-color: rgb(202, 208, 228);
}</style>