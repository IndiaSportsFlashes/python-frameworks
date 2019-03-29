import Axios from 'axios'
const RESOURCE_NAME = '/result'

export default {
  endMatch(payload) {
    return Axios.put(RESOURCE_NAME,payload);
  }

};