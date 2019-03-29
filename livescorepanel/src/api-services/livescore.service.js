import Axios from 'axios'
const RESOURCE_NAME = '/livescore'

export default {
  getLiveMatch(id) {
    return Axios.get(RESOURCE_NAME+"/"+id);
  },
  postLiveMatch(payload){
    return Axios.post(RESOURCE_NAME,payload);
  }
};