<template>
    <div>
        <h1>Sensores</h1>
        <ul>
            <li v-for="sensor in sensores" :key="sensor.id">{{ sensor.nombre }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

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
            });
    }
};
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

p {
    color: black;
    font-family: cursive;
}

input {
    background-color: rgb(39, 84, 231);
}
</style>