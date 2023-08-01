import axios from 'axios';

// default api request settings
const instance = axios.create({
  baseURL: `${window._env_.KUBE_BACKEND_URL}`,
  timeout: 30000,
});

instance.defaults.headers.common['Content-Type'] = 'application/json';
instance.defaults.headers.common['Accept'] = 'application/json';

export function setAxiosToken(token) {
  if (token) {
    instance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete instance.defaults.headers.common['Authorization'];
  }
}

export function parseErrorResponse(error) {
  if (error?.response?.status === 401) {
    console.log("should logout")
  }
  else if (error.request.responseType === 'blob' && error.response.data instanceof Blob) {
    return new Promise((resolve, reject) => {
      let reader = new FileReader();
      reader.onload = () => {
        error.response.data = JSON.parse(reader.result);
        resolve(Promise.reject(error));
      };

      reader.onerror = () => {
        reject(error);
      };

      reader.readAsText(error.response.data);
    });
  } else if (error.request.responseType === 'arraybuffer') {
    if ('TextDecoder' in window) {
      // Decode as UTF-8
      let dataView = new DataView(error.response.data);
      let decoder = new TextDecoder('utf8');
      error.response.data = JSON.parse(decoder.decode(dataView));
      return error;
    } else {
      // Fallback decode as ASCII
      let decodedString = String.fromCharCode.apply(null, new Uint8Array(error.response.data));
      error.response.data = JSON.parse(decodedString);
      return error;
    }
  }
  return error;
}

export function setupInterceptors() {
  instance.interceptors.response.use(
    (response) => {
      return response;
    },
    (error) => {
      if (error.response && error.response.data) {
        error = parseErrorResponse(error);

        return Promise.reject(error);
      }
      return Promise.reject(error);
    }
  );
}

export default instance;
