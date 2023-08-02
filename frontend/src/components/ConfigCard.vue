<script setup>
defineProps(['id'])
const emit = defineEmits(['mapClick']);

function onButtonClick(id) {
    emit("mapClick", id)
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
    margin: 10px;
}

.card-wrapper:hover {
    background-color: rgb(0, 189, 126);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    padding: 20px;
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