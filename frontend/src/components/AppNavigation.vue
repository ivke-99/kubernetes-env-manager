<template>
    <nav class="navbar">
      <ul class="nav-list">
        <RouterLink  to="/">Configmaps</RouterLink>
        <li v-if="authStore.token" @click="logout">Logout</li>
        <RouterLink v-else to="/login">Login</RouterLink>
      </ul>
    </nav>
</template>
<script setup>
import { useAuthStore } from '@/stores/auth.js';
import { useRouter } from 'vue-router';
const authStore = useAuthStore();
const router = useRouter()

function logout() {
  authStore.deleteAxiosToken()
  router.push({name: 'login'})
}
</script>
  
  <style scoped>
  .navbar {
    background-color: #333;
    color: #fff;
    padding: 10px;
  }
  
  .nav-list {
    font-size: 25px;
    list-style: none;
    display: flex;
    gap: 20px;
    justify-content: flex-start;
    padding: 0;
    margin: 0;
  }
  
  .nav-item {
    margin: 0 10px;
  }
  
  </style>