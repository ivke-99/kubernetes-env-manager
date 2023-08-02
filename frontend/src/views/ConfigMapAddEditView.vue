<template>
    <div class="container min-vh-100">
        <div class="row">
            <div v-if="isNotFound">
                <h1 class="alert alert-danger">ConfigMap not found.</h1>
            </div>
            <form v-else class="form-wrapper d-flex align-items-center flex-column w-100"
                style="background: rgba(255, 255, 255, 0.8); border-radius: 8px; padding: 20px;" @submit.prevent="">
                <div class="alert alert-danger" v-for="error in errors" :key="error">{{ error }}</div>
                <div class="form-group w-100">
                    <div class="row">
                        <div class="col-5">
                            <h2>Configmap name</h2>
                            <input id="configMapName" class="form-control" v-model="configMap.name"
                                placeholder="Configmap Name" required>
                        </div>
                    </div>
                    <h2 class="mt-3">Configmap data</h2>
                    <div class="row mb-1" v-for="(item, index) in configMap.data" :key="index">
                        <MapFormField v-model="configMap.data[index]" :index="index" @deleteItem="onFormFieldDeleted">
                        </MapFormField>
                    </div>
                    <div class="d-flex justify-content-center m-5">
                        <button class="btn btn-primary m-1 btn-lg" @click="addEntry">Add new row</button>
                        <button class="btn btn-success submit-button m-1 btn-lg" type="submit"
                            v-dialog="{ yes: submitChanges, no: () => { } }">
                            Submit changes
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>
  
  
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
    let isValid = true
    configMap.value.data.forEach(item => {
        for (const [key] of Object.entries(item)) {
            if (key === "") {
                errors.value.push("Some fields in data are empty.")
                isValid = false
            }
        }
    })
    if (!isValid) return
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
