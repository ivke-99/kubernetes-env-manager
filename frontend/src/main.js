import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import Dialog from 'vue3-dialog';

const app = createApp(App)

app.use(createPinia())
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
