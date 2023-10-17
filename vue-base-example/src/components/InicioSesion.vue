<template>
    <div>
        <h2>Iniciar Sesión</h2>
        <form @submit.prevent="loginUser">
            <input v-model="username" type="text" placeholder="Nombre de Usuario" required>
            <input v-model="password" type="password" placeholder="Contraseña" required>
            <button type="submit">Iniciar Sesión</button>
            <p>¿No estas registrado?</p><a href="RegistrarUsuario.vue">Registrate aqui</a>
        </form>
    </div>
</template>
<script>
/* eslint-disable */
export default {
    data() {
        return {
            DNI: '',
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
                    // Dirigir a Estacionamiento
                })
                .catch(error => {
                    console.error(error);
                });
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
    background-color: rgb(31, 49, 209);
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
a{
    color: white;
    font-family: cursive;
}
</style>
  