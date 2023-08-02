<template>
  <nav class="navbar navbar-dark bg-dark">
    <ul class="nav-list navbar-nav">
      <RouterLink class="nav-item nav-link" to="/">Configmaps</RouterLink>
      <li v-if="authStore.token" @click="logout" class="nav-item nav-link">Logout</li>
      <RouterLink v-else class="nav-item nav-link" to="/login">Login</RouterLink>
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
  router.push({ name: 'login' })
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
  display: flex;
  gap: 15px;
  flex-direction: row;
  justify-content: flex-start;
}
</style>