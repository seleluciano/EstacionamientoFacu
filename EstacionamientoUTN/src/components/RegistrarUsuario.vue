<template>
    <div>
        <h1>ESTACIONAMIENTO UTN</h1>
        <h2>REGISTRAR USUARIO</h2>
        <form @submit.prevent="registerUser">
            <p>Nombre:</p>
            <input v-model="nombre" type="text" placeholder="Nombre" required>
            <p>Apellido:</p>
            <input v-model="apellido" type="text" placeholder="Apellido" required>
            <p>Email:</p>
            <input v-model="telefono" type="email" placeholder="Email" required>
            <p>Usuario:</p>
            <input v-model="username" type="text" placeholder="Nombre de Usuario" required>
            <p>Contraseña:</p>
            <input v-model="password1" type="password" placeholder="Contraseña" required>
            <p>Vuelva a ingresar la contraseña:</p>
            <input v-model="password2" type="password" placeholder="Contraseña" required>
            <p>La contraseña debe tener al menos 8 caracteres con 1 mayuscula,1 minuscula y 1 número</p>
            <button type="submit">REGISTRAR</button>
        </form>
        <p><br>¿Ya estas registrado?</p><button @click="redirectToAbout">Iniciar Sesion</button>
    </div>
</template>
<script>
/* eslint-disable */
import axios from 'axios';

export default {
    data() {
        return {
            first_name: '',
            last_name: '',
            password1: '',
            password2: '',
            email: '',
            username: ''
        }
    },
    methods: {
        registerUser() {
            if (!this.nombre || !this.apellido || !this.email || !this.username || !this.password1 || !this.password2) {
                window.alert('Por favor, complete todos los campos.');
                return;
            }
            if (this.password1 !== this.password2) {
                window.alert('Las contraseñas no coinciden. Vuelva a intentarlo.');
                return;
            }
            axios.post('http://localhost:8000/register/', {
                first_name: this.nombre,
                last_name: this.apellido,
                email: this.email,
                password1: this.password1,
                password2: this.password2,
                username: this.username
            })
                .then(response => {
                    console.log(response);
                    const token = response.data.token;
                    localStorage.setItem('token', token);
                    this.$router.push('/estacionamiento');
                })
                .catch(error => {
                    window.alert('Hubo un problema con el registro. Intentelo nuevamente.');
                    console.error(error);
                });
        },
        redirectToAbout() {
            this.$router.push('/inicio');
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
    font-family: 'Helvetica Neue', sans-serif;
    color: #333;
    margin-bottom: 20px;
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