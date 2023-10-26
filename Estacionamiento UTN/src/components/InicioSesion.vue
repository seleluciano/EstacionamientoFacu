<template>
    <div>
        <h1>ESTACIONAMIENTO UTN</h1>
        <h2>Iniciar Sesión</h2>
        <form @submit.prevent="loginUser">
            <input v-model="username" type="text" placeholder="Nombre de Usuario" required>
            <input v-model="password" type="password" placeholder="Contraseña" required>
            <button @click="Estacionamiento" type="submit">Iniciar Sesión</button>
            <p>¿No estas registrado?</p><button @click="redirectToAbout">Registrese aqui</button>
        </form>
    </div>
</template>
<script>
/* eslint-disable */
import axios from 'axios';
export default {
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        loginUser() {
            axios.post('http://localhost:8000/api/login/', {
                username: this.username,
                password: this.password
            })
                .then(response => {
                    console.log(response);
                    this.$router.push('/Estacionamiento');
                })
                .catch(error => {
                    console.error(error);
                });
        },
        redirectToAbout() {
            this.$router.push('/RegistrarUsuario'); //Redirige a la pagina
        },
        Estacionamiento() {
            this.$router.push('/');
        }
    }
}
</script>
<style>
* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}

body {
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
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

button {
    color: white;
    font-family: 'Helvetica Neue', sans-serif;
    background-color: #007BFF;
    border: none;
    border-radius: 4px;
    padding: 12px 20px;
    margin-top: 10px;
    cursor: pointer;
}
</style>
