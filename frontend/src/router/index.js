import { createRouter, createWebHistory } from 'vue-router'
import ConfigMapsView from '../views/ConfigMapsView.vue'
import ConfigMapAddEditView from '../views/ConfigMapAddEditView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'configmaps',
      component: ConfigMapsView
    },
    {
      path: `/config-map/:name?`,
      props: true,
      name: 'configmap-add-edit',
      component: ConfigMapAddEditView,
    }
  ]
})

export default router
