<template>
 <div class="container">
  <div class="login">
    <h1>{{ msg }}</h1>
    <div class="row">
    <div class="col-md-6">
    <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text"  name="username" class="form-control" 
                />
                
            </div>
            <div class="form-group">
                <label htmlFor="password">Password</label>
                <input type="password" name="password" class="form-control" 
             />
                
            </div>
            <div class="form-group">
                <button class="btn btn-primary">Login</button>
                <router-link to="/register" class="btn btn-link">Register</router-link>
            </div>
        </form>
        
    
    </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>