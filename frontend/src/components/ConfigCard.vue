<script setup>
import { useRouter } from 'vue-router'

defineProps(['id'])
const router = useRouter()

function onButtonClick(id) {
    router.push({
        name: 'configmap-add-edit',
        params: {
            name: id
        }
    })
}
</script>
<template>
    <div @click="onButtonClick(id)" class="card-wrapper">
        <h4>{{ id }}</h4>
    </div>
</template>
<style scoped>
.card-wrapper {
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    padding: 20px;
    width: 300px;
    margin: 10px;
}

h4 {
    margin: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 18px;
    font-weight: bold;
    color: #333;
}
</style>