<template>
    <div>
        <h1>ESTACIONAMIENTO UTN</h1>
        <div class="columns">
            <div class="column">
                <h2>NUMERO</h2>
                <ul v-for="sensor in sensores" :key="sensor.id" class="ID">
                    <li>{{ sensor.id }}</li>
                </ul>
            </div>
            <div class="column">
                <h2>ESTADO</h2>
                <ul v-for="sensor in sensores" :key="sensor.id">
                    <button :class="{ 'Ocupado': sensor.estado, 'Desocupado': !sensor.estado }">
                        {{ sensor.estado ? 'Ocupado' : 'Desocupado' }}
                    </button>
                </ul>
            </div>
        </div>
        <button @click="salir" class="Salir">Salir</button>
    </div>
</template>
<script>
/* eslint-disable */
import axios from 'axios';
export default {
    name: 'APITest',
    data() {
        return {
            sensores: [],
        };
    },
    mounted() {
        // Llamar a la función para cargar sensores
        this.cargarSensores();

        // Configurar un intervalo para cargar sensores cada 1 segundo
        setInterval(this.cargarSensores, 4000);
    },
    methods: {
        cargarSensores() {
            axios.get('http://localhost:8000/sensores/')
                .then(response => {
                    this.sensores = response.data;
                })
                .catch(error => {
                    console.error('Error al cargar los sensores:', error);
                    window.alert('Error al cargar los sensores. Por favor, inténtalo de nuevo más tarde.');
                });
        },
        salir() {
            this.$router.push('/');
        },
    },
};
</script>
  
<style>
body {
    background-color: #71abec;
    font-family: Arial, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 80%;
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
    font-family: 'Times New Roman', sans-serif;
    color: #000000;
    margin-bottom: 20px;
    font-size: 50px;
    /* Tamaño de fuente en píxeles */
}

h2 {
    font-family: 'Times New Roman', sans-serif;
    color: #000000;
    margin-bottom: 20px;
    font-size: 30px;
    /* Tamaño de fuente en píxeles */
}

input {
    background-color: rgb(158, 203, 212);
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    margin: 10px 0;
    width: 100%;
}

a {
    color: #03376e;
    text-decoration: none;
    margin: 10px 0;
    display: inline-block;
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
    margin-top: 8px;
    /* Ajuste para que estén a la misma altura */
    cursor: pointer;
}

button {
    color: white;
    font-family: 'Helvetica Neue', sans-serif;
    background-color: #007BFF;
    border: none;
    border-radius: 4px;
    padding: 12px 20px;
    margin-top: 10px;
    /* Ajuste para que estén a la misma altura */
    cursor: pointer;
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

.Salir {
    color: rgb(255, 255, 255);
    font-family: 'Helvetica Neue', sans-serif;
    background-color: rgb(0, 0, 0);
    border: none;
    border-radius: 4px;
    padding: 12px 20px;
    margin-top: 10px;
    cursor: pointer;
    position: absolute;
    top: 5%;
    right: 5%;
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