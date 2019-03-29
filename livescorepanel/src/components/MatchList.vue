<template>
<div>
    <Header />
    <el-container>
        <SideMenu />
        <el-main>
            <MatchListTemplate />
        </el-main>
    </el-container>
</div>
</template>

<script>
import Header from './Header'
import SideMenu from './SideMenu'
import MatchListTemplate from './MatchListTemplate'

export default {
    name: 'App',
    components: {
        Header,
        SideMenu,
        MatchListTemplate
    }
}
</script>
