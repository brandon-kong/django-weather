<template>
    <div>
        <div id="app">
            <img alt="Vue logo" src="@/assets/logo.png">
            <form submit="login">
                <input type="text" v-model="email" placeholder="email">
                <input type="password" v-model="password" placeholder="password">
                <button type="submit">Login</button>
            </form>

        </div>
    </div>
  </template>

<script>

import axios from 'axios'

export default {
    name: 'App',
    data () {
        return {
            csrf: '',
            isAuthenticated: false,
            email: '',
            password: '',
        }
    },

    mounted () {
        this.getSession()
    },

    methods: {
        login (event) {
            event.preventDefault()
            axios.post("http://localhost:8000/api/login/", {
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.csrf,
                },
                credentials: "include",
                body: JSON.stringify({email: this.email, password: this.password}),
                })
                .then((data) => {
                console.log(data);
                this.isAuthenticated = true
                })
                .catch((err) => {
                console.log(err);
                this.error = "Wrong username or password."
            });
        },

        getSession () {
            axios.post('http://localhost:8000/api/session', {
                credentials: 'include'
            })
                .then(response => {
                    console.log(response.data)
                    if (response.data.isAuthenticated) {
                        this.isAuthenticated = true
                    } else {
                        this.isAuthenticated = false
                        this.getCSRF()
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        },

        getCSRF () {
            axios.post('http://localhost:8000/api/csrf', {
                credentials: 'include'
            })
                .then(response => {
                    console.log(response.data)
                    let csrfToken = response.headers.get("X-CSRFToken");
                    this.csrf = csrfToken
                    console.log(csrfToken);
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}


</script>

<style>

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
