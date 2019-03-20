<template>
  <div id="app">
    <router-view v-if="isLoggedIn"></router-view>
    <LoginPage v-else @TheLogin::loginResult="handleLoginResult" />
  </div>
</template>

<script>
// import LoginPage from './components/LoginPage.vue'
import LoginPage from './components/LoginPage.vue'


export default {
  name: 'app',
  components: {
    LoginPage
  },
  data() {
    return {
      userIsLoggedIn: false
    }
  },
  computed: {
    isLoggedIn() {
      return this.userIsLoggedIn
    }
  },
  methods: {
    handleLoginResult({loginResult}) {
      this.userIsLoggedIn = loginResult
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  overflow-x: hidden;
}
body{
  background: #5e7998;
}
</style>
