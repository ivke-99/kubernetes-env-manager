<script setup>
import { useRouter } from 'vue-router';
import ConfigCard from '../components/ConfigCard.vue';
import { onMounted, ref } from 'vue';
import { getConfigmaps } from '@/api/configmap';
const router = useRouter()
const configMaps = ref([])

onMounted(() => {
  getConfigmaps().then((res) => {
    configMaps.value = res?.data
  })
})

function onAddClick(id) {
  let params = {}
  if (id) {
    params = {
      name: id
    }
  }
  router.push({
    name: 'configmap-add-edit',
    params: params
  })
}
</script>

<template>
  <div class="header-wrapper">
    <button @click="onAddClick()">Add a configmap</button>
  </div>
  <div class="configmaps">
    <ConfigCard v-for="map in configMaps" :key="map?.name" :id="map?.name" @map-click="onAddClick" />
  </div>
</template>

<style scoped>
.configmaps {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.header-wrapper {
  display: flex;
  justify-content: center;
  margin: 25px;
}

.header-wrapper button {
  font-size: 25px;
}
</style>