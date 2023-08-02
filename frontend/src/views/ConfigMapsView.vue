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
  <div class="container text-center">
    <button type="button" class="btn btn-light mb-5 mt-5 btn-lg" @click="onAddClick()">Add a configmap</button>
    <div class="row row-cols-2">
      <div class="col" v-for="map in configMaps" :key="map?.name" :id="map?.name">
        <ConfigCard :id="map?.name" @map-click="onAddClick" />
      </div>
    </div>
  </div>
</template>