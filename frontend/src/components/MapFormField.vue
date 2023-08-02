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
    <div class="col-5">
        <input class="form-control" :value="Object.keys(modelValue)[0]" placeholder="Key"
            @input="updateModelValue({ [$event.target.value]: Object.values(modelValue)[0] })" required />
    </div>
    <div class="col-5">
        <input class="form-control" :value="Object.values(modelValue)[0]" placeholder="Value"
            @input="updateModelValue({ [Object.keys(modelValue)[0]]: $event.target.value })" />
    </div>
    <div class="col-2">
        <button type="button" class="btn btn-danger" @click="deleteEntry">DELETE</button>
    </div>
</template>
