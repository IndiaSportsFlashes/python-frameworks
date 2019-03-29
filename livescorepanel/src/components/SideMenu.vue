<template>
<el-aside class="sidemenu" width="auto">
    <div style="margin: 20px 10px; text-align: left;">
        <el-button v-if="isCollapse" type="plain" @click="expand"><i class="el-icon-tickets"></i></el-button>
        <el-button v-else type="plain" @click="collapse"><i class="el-icon-caret-left"></i></el-button>
    </div>
    <el-menu default-active="2" class="el-menu-vertical-demo" :collapse="isCollapse" :router="true" style="border-right: none; text-align: left; margin-right: 10px;">
        <el-submenu index="1">
            <template slot="title">
                <i class="el-icon-menu"></i>
                <span slot="title">Match</span>
            </template>
            <el-menu-item index="1-1" :route="{name:'MatchCreation'}">Create Match
            </el-menu-item>
            <el-menu-item index="1-2" :route="{name:'MatchList'}">Match List</el-menu-item>
        </el-submenu>
        <el-submenu index="2">
            <template slot="title">
                <i class="el-icon-menu"></i>
                <span slot="title">LIVE</span>
            </template>
            <el-menu-item index="1-1" :route="{name:'LiveMatchList'}">LIVE Panel</el-menu-item>
            <!-- <el-menu-item index="1-2">LIVE Comment</el-menu-item> -->
        </el-submenu>
    </el-menu>
</el-aside>
</template>

<script>
export default {
    name: "sidemenu",
    data() {
        return {
            isCollapse: true
        };
    },
    methods: {
        collapse() {
            this.isCollapse = true
        },
        expand() {
            this.isCollapse = false
        },
    }
}
</script>
