import { createRouter, createWebHistory } from 'vue-router'
import ConfigMapsView from '../views/ConfigMapsView.vue'
import ConfigMapAddEditView from '../views/ConfigMapAddEditView.vue'
import LoginView from '@/views/LoginView.vue'
import { useAuthStore } from '@/stores/auth.js';


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
    },
    {
      path: `/login`,
      name: 'login',
      component: LoginView,
    }
  ]
})

router.beforeEach(async (to) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const auth = useAuthStore();

  if (authRequired && !auth.token) {
      auth.returnUrl = to.fullPath;
      return '/login';
  }
});

export default router
