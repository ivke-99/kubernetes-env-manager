<template>
    <section class="vh-50">
        <div class="container py-5 h-50">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card bg-dark text-white" style="border-radius: 1rem;">
                        <div class="card-body p-5 text-center">

                            <div class="mb-md-5 mt-md-4 pb-5">

                                <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                                <p class="text-white-50 mb-5">Please enter your username and password!</p>
                                <div v-if="error">
                                    <p class="text-danger mb-5">{{ error }}</p>
                                </div>
                                <div class="form-outline form-white mb-4">
                                    <input id="username" v-model="state.username" class="form-control form-control-lg" />
                                    <label class="form-label" for="username">Username</label>
                                </div>

                                <div class="form-outline form-white mb-4">
                                    <input type="password" v-model="state.password" id="password"
                                        class="form-control form-control-lg" />
                                    <label class="form-label" for="password">Password</label>
                                </div>


                                <button class="btn btn-outline-light btn-lg px-5" type="submit"
                                    @click="handleSubmit">Login</button>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
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