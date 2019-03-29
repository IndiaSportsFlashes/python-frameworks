import Vue from 'vue'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import router from './router'
import store from './store'
import App from './App.vue'
import Axios from 'axios'
import CKEditor from '@ckeditor/ckeditor5-vue';

Axios.defaults.baseURL = process.env.API_ENDPOINT;
Axios.defaults.headers={
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' +'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTM1OTY5MjIsIm5iZiI6MTU1MzU5NjkyMiwianRpIjoiYTEwNGVhYWYtYjQyMS00Yjk5LWI2YzItOWNmMDVjMzc5NTdlIiwiZXhwIjoxNTU0ODA2NTIyLCJpZGVudGl0eSI6Imdrc3JpcmFtIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.OSWPa0XBlISdGSUAdCw38xqffHTkd6lfDyD8Xqe87tE'}
Vue.config.productionTip = false

Vue.use(ElementUI, { locale })
Vue.use( CKEditor );


new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
