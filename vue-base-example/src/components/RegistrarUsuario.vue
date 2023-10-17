<template>
    <div>
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
            <p>Nombre de Usuario</p>
            <input v-model="username" type="text" placeholder="Nombre de Usuario" required>
            <p>Contraseña:</p>
            <input v-model="password" type="password" placeholder="Contraseña" required>
            <button type="submit">Registrar</button>
        </form>
        <p>¿Ya estas registrado?</p><a href="InicioSesion.vue">Iniciar Sesion</a>
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

.columns {
    display: flex;
    justify-content: space-between;
}

.column {
    flex: 1;
    margin-right: 10px;
}
</style>