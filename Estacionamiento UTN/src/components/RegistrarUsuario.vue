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
        <p><br>¿Ya estas registrado?</p><button @click="redirectToAbout">Iniciar Sesion</button>
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
    height: 150vh;
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