<template>
<div>
    <Header />
    <el-container>
        <SideMenu />
        <el-main>
            <LiveMatchListTemplate />
        </el-main>
    </el-container>
</div>
</template>

<script>
import Header from './Header'
import SideMenu from './SideMenu'
import LiveMatchListTemplate from './LiveMatchListTemplate'

export default {
    name: 'App',
    components: {
        Header,
        SideMenu,
        LiveMatchListTemplate
    },
    data() {
        return {
            info: null
        }
    }
}
</script>
