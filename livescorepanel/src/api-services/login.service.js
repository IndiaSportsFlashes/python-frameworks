import Axios from 'axios'
const RESOURCE_NAME = '/login';
let payload ={ "username": "sfankur", "password": "ankur" }

export default {
  getAll() {
    return Axios.post(RESOURCE_NAME,payload);
  }
};