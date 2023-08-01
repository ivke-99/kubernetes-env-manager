<script setup>
import MapFormField from '../components/MapFormField.vue';
import { ref, onMounted } from 'vue';
import { getConfigmap, addConfigMap, updateConfigMap } from '@/api/configmap';
import { useRouter } from 'vue-router';

const props = defineProps(['name'])
const router = useRouter()
const isNotFound = ref(false)
const errors = ref([])
const configMap = ref({
    name: "",
    data: []
})

onMounted(() => {
    if (props.name) {
        getConfigmap(props.name).then((res) => {
            let newMap = res?.data
            if (newMap?.data) {
                newMap.data = formatConfigMapData(newMap.data)
            } else {
                newMap.data = []
            }
            configMap.value = newMap
        }).catch(() => {
            isNotFound.value = true
        })
    }
})

function hasDuplicateKeys(obj) {
    const seenKeys = new Set();

    for (const item of obj.data) {
        for (const key of Object.keys(item)) {
            if (seenKeys.has(key)) {
                return true;
            }
            seenKeys.add(key);
        }
    }

    return false;
}

function formatConfigMapData(obj) {
    return Object.entries(obj).map(([key, value]) => ({ [key]: value }));
}

function onFormFieldDeleted(val) {
    configMap.value.data.splice(val, 1)
}
function addEntry() {
    configMap.value.data.push({
        "": ""
    })
}

function submitChanges() {
    errors.value = []
    if (configMap.value.name === "") {
        errors.value.push("Configmap name cannot be empty.")
        return;
    }
    configMap.value.data.forEach(item => {
        for (const [key] of Object.entries(item)) {
            if (key === "") {
                errors.value.push("Some fields in data are empty.")
                return;
            }
        }
    })
    if (hasDuplicateKeys(configMap.value)) {
        errors.value.push("Duplicate keys in data.")
        return;
    }
    const formattedData = configMap.value.data.reduce((acc, curr) => {
        Object.keys(curr).forEach(key => {
            acc[key] = curr[key];
        });
        return acc;
    }, {});
    const postItem = { name: configMap.value.name, data: formattedData }
    if (props?.name) {
        updateConfigMap(props.name, postItem).then(() => {
            router.push({ name: "configmaps" })
        }).catch((err) => {
            Object.entries(err?.response?.data?.errors).forEach((key, val) => {
                errors.value.push(val)
            })
        })
    } else {
        addConfigMap(postItem).then(() => {
            router.push({ name: "configmaps" })
        }).catch((err) => {
            Object.entries(err?.response?.data?.errors).forEach(val => {
                errors.value.push(val)
            })
        })
    }
}

</script>
<template>
    <div v-if="isNotFound">
        <h1>ConfigMap not found. </h1>
    </div>
    <div v-else class="form-wrapper">
        <h1 class="form-title">Add/Edit a configmap</h1>
        <h2 class="form-errors" v-for="error in errors" :key="error">{{ error }}</h2>
        <h2>Configmap name</h2>
        <input v-model="configMap.name" placeholder="Configmap Name" required>
        <h2>Configmap data</h2>
        <div class="form-items-wrapper">
            <div v-for="(item, index) in configMap.data" :key="index">
                <MapFormField v-model="configMap.data[index]" :index="index" @deleteItem="onFormFieldDeleted">
                </MapFormField>
            </div>
        </div>
        <button @click="addEntry">Add new row</button>
        <button class="submit-button" v-dialog="{
            yes: submitChanges,
            no: () => { }
        }">Submit changes</button>
    </div>
</template>
<style scoped>
.form-wrapper {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.form-wrapper button,
.form-wrapper input,
.form-wrapper h2 {
    align-self: center;
    font-size: 18px;
}

.form-items-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.form-errors {
    background-color: #6b1a1a;
}

.form-title {
    display: flex;
    justify-content: center;
    margin: 20px 0;
    font-size: 24px;
}

.submit-button {
    background-color: olive;
    font-size: 30px !important;
}
</style>