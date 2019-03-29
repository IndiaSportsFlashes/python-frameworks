<template>
<div>
    <Header />
    <el-container>
        <SideMenu />
        <el-main>
            <LiveScoreCard />
            <LiveScoreTemplate />
        </el-main>
    </el-container>
</div>
</template>

<script>
import Header from './Header'
import SideMenu from './SideMenu'
import LiveScoreCard from './LiveScoreCard'
import LiveScoreTemplate from './LiveScoreTemplate'

export default {
    name: 'App',
    components: {
        Header,
        SideMenu,
        LiveScoreCard,
        LiveScoreTemplate
    },
    data() {
        return {
            info: null
        }
    }
}
</script>
