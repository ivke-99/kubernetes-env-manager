<script setup>
import { RouterView } from 'vue-router'
import AppNavigation from './components/AppNavigation.vue';
import { setupInterceptors } from './api/base.js';

setupInterceptors()
</script>

<template>
  <header>
    <AppNavigation />
  </header>
  <RouterView />
</template>