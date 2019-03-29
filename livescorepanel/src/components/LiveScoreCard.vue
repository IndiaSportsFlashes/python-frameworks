<template>
<el-card class="score-card" body-style="padding:0px" shadow="always" v-if="this.$store.state.showScoreCard">
    <div slot="header" style="height: auto;">
        <h4 class="scoreCard">{{this.$store.state.scoreCardHeader.battingTeam}}</h4>
        <h4 class="scoreCard">{{this.$store.state.scoreCardHeader.runs + "/" + this.$store.state.scoreCardHeader.wickets + "(" + this.$store.state.scoreCardHeader.over + " ovs)"}}</h4>
        <h4 class="scoreCard">{{this.$store.state.scoreCardHeader.currentRunRate}}</h4>
    </div>
    <table style="width:100% ; font-size:12px;">
        <tr style=" background-color: #eee;">
            <th>Batsman</th>
            <th>R</th>
            <th>B</th>
            <th>4s</th>
            <th>6s</th>
            <th>SR</th>
        </tr>
        <tr >
            <td >{{this.$store.state.playersName.stickerName}}</td>
            <td>{{this.$store.state.scoreCard.striker_run}}</td>
            <td>{{this.$store.state.scoreCard.striker_balls}}</td>
            <td>{{this.$store.state.scoreCard.striker_4}}</td>
            <td>{{this.$store.state.scoreCard.striker_6}}</td>
            <td>{{this.$store.state.scoreCard.striker_strikerate}}</td>
        </tr>
        <tr>
            <td>{{this.$store.state.playersName.nonStickerName}}</td>
            <td>{{this.$store.state.scoreCard.non_striker_run}}</td>
            <td>{{this.$store.state.scoreCard.non_striker_balls}}</td>
            <td>{{this.$store.state.scoreCard.non_striker_4}}</td>
            <td>{{this.$store.state.scoreCard.non_striker_6}}</td>
            <td>{{this.$store.state.scoreCard.non_striker_strikerate}}</td>
        </tr>
    </table>
    <table style="width:100% ; font-size:12px;">
        <tr style=" background-color: #eee;">
            <th>Bowler</th>
            <th>O</th>
            <th>R</th>
            <th>M</th>
            <th>W</th>
            <th>EC</th>
        </tr>
        <tr>
            <td>{{this.$store.state.playersName.curBowlerName}}</td>
            <td>{{this.$store.state.scoreCard.cur_bowler_over}}</td>
            <td>{{this.$store.state.scoreCard.cur_bowler_run}}</td>
            <td>{{this.$store.state.scoreCard.cur_bowler_mai}}</td>
            <td>{{this.$store.state.scoreCard.cur_bowler_wic}}</td>
            <td>{{this.$store.state.scoreCard.cur_bowler_eco}}</td>
        </tr>
        <tr>
            <td>{{this.$store.state.scoreCard.preBowlerName}}</td>
            <td>{{this.$store.state.scoreCard.prv_bowler_over}}</td>
            <td>{{this.$store.state.scoreCard.prv_bowler_run}}</td>
            <td>{{this.$store.state.scoreCard.prv_bowler_mai}}</td>
            <td>{{this.$store.state.scoreCard.prv_bowler_wic}}</td>
            <td>{{this.$store.state.scoreCard.prv_bowler_eco}}</td>
        </tr>
    </table>
    <!-- <span>{{this.$store.state.scoreCard}}</span> -->
</el-card>
</template>

<script>
export default {
    name: "sidemenu",
    data() {
        return {
            scoreCardHeader:false
        }
    },
    created() {
            if(this.$store.state.scoreCardHeader.battingTeam)
                this.scoreCardHeader= true
            else
                this.scoreCardHeader= false
    }
}
</script>

<style>
.score-card {
    width: auto;
}

.el-card__header {
    padding: 0px
}

h4.scoreCard,
h5.batsman {
    display: inline-block;
    padding-left: 5px;
    padding-right: 5px
}
</style>
