<template>
    <div>
        <h1>ESTACIONAMIENTO UTN</h1>
        <h2>Iniciar Sesión</h2>
        <form @submit.prevent="loginUser">
            <input v-model="username" type="text" placeholder="Nombre de Usuario" required>
            <input v-model="password" type="password" placeholder="Contraseña" required>
            <button type="submit">INICIAR SESION</button>
            <p><br>¿No estás registrado?</p><button @click="redirectToAbout">Registrese aquí</button>
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
            password: '',
        }
    },
    methods: {
        loginUser() {
            axios.post('http://localhost:8000/login_user/', {
                username: this.username,
                password: this.password
            })
                .then(response => {
                    console.log(response);
                    const token = response.data.token;
                    localStorage.setItem('token', token);
                    console.log('Redirigiendo a /estacionamiento');
                    this.$router.push('/estacionamiento');
                })
                .catch(error => {
                    window.alert('Los datos ingresados son incorrectos, Intentelo nuevamente');
                    console.error(error);
                });
        },
        redirectToAbout() {
            this.$router.push('/registro'); //Redirige a la pagina
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
    font-size: 50px; /* Tamaño de fuente en píxeles */
}

h2 {
    font-family: 'Times New Roman', sans-serif;
    color: #000000;
    margin-bottom: 20px;
    font-size: 30px; /* Tamaño de fuente en píxeles */
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