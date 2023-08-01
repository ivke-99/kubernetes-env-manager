import axios from './base.js';

export const getConfigmaps = () => {
    return axios.get(`/configmap/`);
};

export const getConfigmap = (id) => {
    return axios.get(`/configmap/${id}/`)
}

export const addConfigMap = (data) => {
    return axios.post(`/configmap/`, data)
}

export const updateConfigMap = (id, data) => {
    return axios.put(`/configmap/${id}/`, data)
}