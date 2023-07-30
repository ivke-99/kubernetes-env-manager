<script setup>
const props = defineProps(['modelValue', 'index']);
const emit = defineEmits(['update:modelValue', 'deleteItem']);

function updateModelValue(value) {
    emit("update:modelValue", value)
}
function deleteEntry() {
    emit("deleteItem", props.index)
}
</script>

<template>
    <div class="config-map-wrapper" v-for="(val, key) in modelValue" :key="key">
        <input class="config-key" :value="key" @input="updateModelValue({ [$event.target.value]: val })" />
        <input class="config-val" :value="val" @input="updateModelValue({ [key]: $event.target.value })" />
        <button @click="deleteEntry">DELETE</button>
    </div>
</template>
<style scoped>
.config-map-wrapper {
    display: flex;
    max-width: 500px;
    margin: 0 auto;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
}

.config-key,
.config-val {
    flex: 1;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

.config-key {
    margin-right: 5px;
}

.config-val {
    margin-left: 5px;
}
</style>
