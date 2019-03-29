import Axios from 'axios'
const RESOURCE_NAME = '/match'


export default {
  getMatchList(status) {
    return Axios.get(RESOURCE_NAME+"?status="+status);
  },
  makeMatchLive(payload) {
    return Axios.put(RESOURCE_NAME,payload);
  },
  matchCreation(payload) {
    return Axios.post(RESOURCE_NAME,payload);
  },
  getMatch(id) {
    return Axios.get(RESOURCE_NAME+"?id="+id);
  }

};