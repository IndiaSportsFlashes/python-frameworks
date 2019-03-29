<template>
<div class="LoginPage" align="center" style="margin: auto;padding: 200px;">
    <el-card class="box-card">
        <div slot="header" class="clearfix">
            <el-row>
                <img src="../assets/logo.png">
                    </el-row>
                <span>Cricket Score Panel</span>
        </div>
        <div style="margin-top: 15px;">
            <el-input placeholder="Enter Username" v-model="username">
                <template slot="prepend"><i class="el-icon-message"></i></template>
            </el-input>
        </div>
        <div style="margin-top: 15px;">
            <el-input placeholder="Enter Password" v-model="password" show-password>
                <template slot="prepend"><i class="el-icon-question"></i></template>
            </el-input>
        </div>
        <div style="margin-top: 15px;">
            <el-button type="primary" @click="logIn">Login</el-button>
        </div>
    </el-card>
</div>
</template>

<script>
export default {
    name: "LoginPage",
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        logIn() {
            this.$router.replace({
                name: "MatchList"
            });
            this.$emit('LoginPage::loginResult', {
                loginResult: true
            })
        }
    }
}
</script>

<style scoped>
text {
    font-size: 14px;
}

.item {
    margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}

.box-card {
    width: 480px;
}
</style>
