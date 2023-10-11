<template>
    <div>
        <h1>ESTACIONAMIENTO</h1>
        <ul>
            <li v-for="sensor in sensores" :key="sensor.id">{{ sensor.nombre }}</li>
        </ul>
    </div>
</template>

<script>
/* eslint-disable */ 
import axios from 'axios'
export default {
    data() {
        return {
            clientes: [],
            sensores: []
        };
    },
    mounted() {
        axios.get('http://localhost:8000/api/sensores/')
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
    background-color: aquamarine;
    width: 100%;
    height: 80%;
}

p,h1 {
    color: black;
    font-family: cursive;
}

input {
    background-color: rgb(10, 64, 240);
}
</style>