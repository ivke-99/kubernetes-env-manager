import { defineStore } from 'pinia'
import { setAuthAxiosToken } from '@/api/base.js'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: "",
  }),
  actions: {
    setAxiosToken(token) {
      this.token = token
      setAuthAxiosToken(token)
    },
    deleteAxiosToken() {
      this.token = ""
    }
  },
  persist: {
    storage: sessionStorage
  }
})
