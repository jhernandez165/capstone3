import axios from 'axios';

export function setupAuthInterceptor() {
  axios.interceptors.request.use(
    config => {
      const token = localStorage.getItem(process.env.REACT_APP_TOKEN_NAME);
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
      }
      return config;
    },
    error => {
      return Promise.reject(error);
    }
  );
}