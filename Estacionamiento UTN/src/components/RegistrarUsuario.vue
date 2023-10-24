<template>
    <div>
        <h1>ESTACIONAMIENTO UTN</h1>
        <h2>REGISTRAR USUARIO</h2>
        <form @submit.prevent="registerUser">
            <p>Nombre:</p>
            <input v-model="nombre" type="text" placeholder="Nombre" required>
            <p>Apellido:</p>
            <input v-model="apellido" type="text" placeholder="Apellido" required>
            <p>Telefono:</p>
            <input v-model="telefono" type="number" placeholder="Telefono" required>
            <p>DNI:</p>
            <input v-model="DNI" type="number" placeholder="DNI" required>
            <p>Nombre de Usuario:</p>
            <input v-model="username" type="text" placeholder="Nombre de Usuario" required>
            <p>Contraseña:</p>
            <input v-model="password" type="password" placeholder="Contraseña" required>
            <button @click="Estacionamiento" type="submit">Registrar</button>
        </form>
        <p>¿Ya estas registrado?</p><button @click="redirectToAbout">Iniciar Sesion</button>
    </div>
</template>
<script>
/* eslint-disable */
export default {
    data() {
        return {
            nombre: '',
            apellido: '',
            telefono: '',
            DNI: '',
            username: '',
            password: ''
        }
    },
    methods: {
        registerUser() {
            axios.post('http://localhost:8000/api/register/', {
                nombre: this.nombre,
                apellido: this.apellido,
                telefono: this.telefono,
                DNI: this.DNI,
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
            this.$router.push('/InicioSesion'); //Redirige a la pagina
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
    background-color: beige;
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