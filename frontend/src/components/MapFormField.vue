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
    <div class="config-map-wrapper">
        <input class="config-key" :value="Object.keys(modelValue)[0]"
            @input="updateModelValue({ [$event.target.value]: Object.values(modelValue)[0] })" />
        <input class="config-val" :value="Object.values(modelValue)[0]"
            @input="updateModelValue({ [Object.keys(modelValue)[0]]: $event.target.value })" />
        <button @click="deleteEntry">DELETE</button>
    </div>
</template>
<style scoped>
.config-map-wrapper {
    display: flex;
}

.config-key,
.config-val {
    padding: 5px;
    width: 400px;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    margin: 1px;
}
</style>
