<template>
  <div id="app">
    <Dashboard />
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
//import Login from './components/Login.vue'
//import Register from './components/Register.vue'
import Dashboard from './components/Dashboard.vue'

export default {
  name: 'app',
  components: {
    Dashboard
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
}
</style>
