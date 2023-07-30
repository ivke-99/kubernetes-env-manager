<script setup>
import MapFormField from '../components/MapFormField.vue';
import { ref } from 'vue'

const items = ref([{
    "SOME_KEY": "SOME_VALUE",

}, {
    "OTHER_KEY": "SOME_VALUE",

}, {
    "OTHER_KEY23": "SOME_VALUE",

}, {
    "OTHER_KEY44": "SOME_VALUE",

}, {
    "SOME_KEY": "SOME_VALUE",

}])
function onFormFieldDeleted(val) {
    items.value.splice(val, 1)
}
</script>
<template>
    <div class="form-wrapper">
        <h1 class="form-title">Add/Edit a configmap</h1>
        <div class="form-items-wrapper" v-for="(item, index) in items" :key="index">
            <MapFormField v-model="items[index]" :index="index" @deleteItem="onFormFieldDeleted"></MapFormField>
        </div>
    </div>
</template>
<style scoped>
.form-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.form-title {
    display: flex;
    /* Set display flex explicitly for h1 */
    justify-content: center;
    margin: 20px 0;
    font-size: 24px;
}
</style>