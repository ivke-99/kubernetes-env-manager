import axios from './base.js';

export const login = (data) => {
    return axios.post(`/auth/login/`, data);
};