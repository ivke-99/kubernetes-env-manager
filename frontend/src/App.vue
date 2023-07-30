<script setup>
import { RouterView } from 'vue-router'
import AppNavigation from './components/AppNavigation.vue';
</script>

<template>
  <header>
    <AppNavigation />
  </header>

  <RouterView />
</template>