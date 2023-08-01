<template>
    <div class="login">
        <h2>Login</h2>
        <form @submit.prevent="handleSubmit">
            <div>
                <label for="username">Username:</label>
                <input type="text" v-model="state.username" required autocomplete="username" />
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" v-model="state.password" required autocomplete="current-password" />
            </div>
            <button type="submit">Login</button>
        </form>
        <div v-if="error" class="error">{{ error }}</div>
    </div>
</template>
  
<script setup>
import { ref } from 'vue';
import { login } from '@/api/auth.js'
import { useAuthStore } from '@/stores/auth.js';
import { useRouter } from 'vue-router';

const state = ref({
    username: '',
    password: '',
});
const store = useAuthStore()
const router = useRouter()
const error = ref('')

const handleSubmit = () => {
    login(state.value).then((res) => {
        store.setAxiosToken(res?.data?.access_token)
        router.push({ name: "configmaps" })
    }).catch(() => {
        error.value = "Invalid username or password."
    })

};
</script>
  
<style>
.login {
    margin: 0 auto;
    max-width: 300px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.login h2 {
    margin-bottom: 10px;
}

.login label {
    display: block;
    margin-bottom: 5px;
}

.login input {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
}

.login button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.login .error {
    color: red;
    margin-top: 10px;
}
</style>