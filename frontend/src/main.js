import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import Dialog from 'vue3-dialog';
import piniaPluginPersistedState from "pinia-plugin-persistedstate"

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedState)
app.use(pinia)
app.use(router)
app.use(Dialog, {
    message: 'Are you sure?',
    buttons: {
        yes: {
            text: 'Yes',
        },
        no: {}
    },
    presets: {
        remove: {
            message: 'Do you want to delete this?',
            buttons: ['cancel', 'remove']
        }
    },
})
app.mount('#app')
