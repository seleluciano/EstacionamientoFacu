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
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color:beige;
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

a {
    color: black;
    font-family: cursive;
}

button {
    color: white;
    font-family: cursive;
    background-color: black;
}
</style>
  