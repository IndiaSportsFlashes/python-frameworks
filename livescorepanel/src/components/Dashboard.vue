<template>
<section class="el-container">
  <aside class="el-aside" style="width: 200px;background:#000;">
    <h3>SF Score Panel</h3>
    <el-row class="tac">
      <el-col :span="12">
        <h5>Home</h5>
      </el-col>
      <el-col :span="12">
        <h5>Teams</h5>
      </el-col>
      <el-col :span="12">
        <h5>Formats</h5>
      </el-col>
      <el-col :span="12">
        <h5>Match</h5>
      </el-col>
    </el-row>
  </aside>
  <section class="el-container is-vertical">
    <header class="el-header" style="height: 60px;">

    </header> 
    <main class="el-main">
       <el-steps :active="1">
          <el-step title="Step 1" description="Some description"></el-step>
          <el-step title="Step 2" description="Some description"></el-step>
          <el-step title="Step 3" description="Some description"></el-step>
        </el-steps>  
    </main> 
    <footer class="el-footer" style="height: 60px;">Footer</footer>
    </section>
  </section>
</template>

<script>


</script>
<style>
@import url("//unpkg.com/element-ui@2.6.1/lib/theme-chalk/index.css");
</style>
