<template>
<div>
    <Header />
    <el-container>
        <SideMenu />
        <el-main>
            <MatchCreationTemplate />
        </el-main>
    </el-container>
</div>
</template>

<script>
import Header from './Header'
import SideMenu from './SideMenu'
import LiveScoreCard from './LiveScoreCard'
import MatchCreationTemplate from './MatchCreationTemplate'

export default {
    name: 'App',
    components: {
        Header,
        SideMenu,
        MatchCreationTemplate
    },
    data() {
        return {
            info: null
        }
    }
}
</script>
