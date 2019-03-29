<template>
<div id="matchlist">
    <el-tabs type="border-card" style="height: 85vh; border: 1px solid #eee ; font-size:15px; font-weight:500;">
        <el-tab-pane label="Upcoming">
            <el-table stripe :data="upcomingList.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))" style="width: auto">
                <el-table-column type="index" width="50">
                </el-table-column>
                <el-table-column label="Name" prop="name">
                </el-table-column>
                <el-table-column label="Date" prop="date">
                </el-table-column>
                <el-table-column label="Venue" prop="venue">
                </el-table-column>
                <el-table-column label="Country" prop="country">
                </el-table-column>
                <el-table-column label="Toss" prop="toss">
                </el-table-column>
                <el-table-column align="right">
                    <template slot="header">
                        <el-input v-model="search" size="mini" placeholder="Type to search" />
                    </template>
                    <template slot-scope="scope">
                        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
                        <el-button size="mini" @click="startMatchForm(scope.$index, scope.row)">Make Live</el-button>
                        <el-dialog title="START MATCH" :visible.sync="dialogFormVisible" style="text-align:center; font-size:50px; font-weight:600;">
                            <el-form style="text-align:right;  padding:70px;  border: 3px solid #eee ;">
                                <el-form-item label="Won_The_Toss" :label-width="formLabelWidth">
                                    <el-select v-model="toss" placeholder="Select">
                                        <el-option v-for="item in selectedTeam" :key="item.id" :label="item.name" :value="item.id">
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                                <el-form-item label="Bating" :label-width="formLabelWidth">
                                    <el-select v-model="team_a" placeholder="Select">
                                        <el-option v-for="item in selectedTeam" :key="item.id" :label="item.name" :value="item.id">
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                            </el-form>
                            <span slot="footer" class="dialog-footer">
                        <el-button @click="dialogFormVisible = false">Cancel</el-button>
                        <el-button type="primary" @click="handleMakeLive(scope.$index, scope.row)">Live</el-button>
                    </span>
                        </el-dialog>
                    </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="Past">
            <el-table stripe :data="pastList.filter(data => !searchPast || data.name.toLowerCase().includes(searchPast.toLowerCase()))" style="width: auto " height="700">
                <el-table-column type="index" width="50">
                </el-table-column>
                <el-table-column label="Name" prop="name">
                </el-table-column>
                <el-table-column label="Date" prop="date">
                </el-table-column>
                <el-table-column label="Venue" prop="venue">
                </el-table-column>
                <el-table-column label="Country" prop="country">
                </el-table-column>
                <el-table-column label="Toss" prop="toss">
                </el-table-column>
                <el-table-column align="right">
                    <template slot="header">
                        <el-input v-model="searchPast" size="mini" placeholder="Type to search" />
                    </template>
                    <template slot-scope="scope">
                        <el-button disabled size="mini" @click="handleView(scope.$index, scope.row)">View</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>
    </el-tabs>
</div>
</template>

<script>
import match from '../api-services/match.service'
import { constants } from 'fs';

export default {
    name: "matchlist",
    data() {
        return {
            upcomingList: [],
            pastList: [],
            search: '',
            searchPast: '',
            dialogFormVisible: false,
            toss: '',
            team_a: '',
            formLabelWidth: 'auto',
            team: [{
                    "id": 1,
                    "name": "Pakistan",
                    "status": true
                },
                {
                    "id": 2,
                    "name": "Sri Lanka",
                    "status": true
                },
                {
                    "id": 3,
                    "name": "India",
                    "status": true
                },
                {
                    "id": 4,
                    "name": "England",
                    "status": true
                }
            ],
            team_enum: {
                1: 'Pakistan',
                2: 'Sri Lanka',
                3: 'India',
                4: 'England'
            },
            selectedTeam: []
        }
    },
    methods: {
        handleEdit(index, row) {
            this.$router.replace({
                name: "MatchEdit",
                params: {
                    id: row['id']
                }
            })
        },
        handleView(index, row) {
            this.$router.replace({
                name: "LiveScorePanel",
                params: {
                    id: row['id']
                }
            })
        },
        handleMakeLive(index, row) {
            this.dialogFormVisible = false
            let key, team_b;
            for (key in this.selectedTeam) {
                if (this.team_a != this.selectedTeam[key]['id']) {
                    team_b = this.selectedTeam[key]['id']
                }
            }
            console.log(this.team_a)
            console.log(team_b)
            console.log(this.selectedTeam)
            let payload = {
                "id": row['id'],
                "team_a": this.team_a,
                "team_b": team_b,
                "toss": this.toss
            }
            match.makeMatchLive(payload)
                .then(response => {
                    this.$notify({
                        title: 'Success',
                        message: 'Match is LIVE',
                        type: 'success'
                    });
                    this.$router.replace({
                        name: "LiveMatchList"
                    });
                })
                .catch(e => {
                    console.log(e)
                })
        },
        startMatchForm(index, row) {
            this.dialogFormVisible = true
            let key;
            let selected = {};
            this.selectedTeam=[]
            for (key in this.team) {
                if (row['team_a'] == this.team[key]['id'] || row['team_b'] == this.team[key]['id']) {
                    selected['id'] = this.team[key]['id']
                    selected['name'] = this.team[key]['name']
                    this.selectedTeam.push(selected)
                    selected = {}
                }
            }
        }

    },
    created() {
        match.getMatchList("UPCOMING")
            .then(response => {
                let data = response.data.data
                let match
                let upcomingMatchData = {}
                for (match in data) {
                    upcomingMatchData['id'] = data[match]['id']
                    upcomingMatchData['team_a'] = data[match]['team_a']
                    upcomingMatchData['team_b'] = data[match]['team_b']
                    upcomingMatchData['name'] = data[match]['name']
                    upcomingMatchData['date'] = data[match]['date']
                    upcomingMatchData['venue'] = data[match]['venue']
                    upcomingMatchData['country'] = this.team_enum[data[match]['country_id']]
                    upcomingMatchData['toss'] = this.team_enum[data[match]['toss']]
                    this.upcomingList.push(upcomingMatchData)
                    upcomingMatchData = {}
                }
            })
            .catch(e => {
                this.errors.push(e)
            })
        match.getMatchList("PAST")
            .then(response => {
                let data = response.data.data
                let match
                let pastMatchData = {}
                for (match in data) {
                    pastMatchData['id'] = data[match]['id']
                    pastMatchData['name'] = data[match]['name']
                    pastMatchData['date'] = data[match]['date']
                    pastMatchData['venue'] = data[match]['venue']
                    pastMatchData['country'] = this.team_enum[data[match]['country_id']]
                    pastMatchData['toss'] = this.team_enum[data[match]['toss']]
                    this.pastList.push(pastMatchData)
                    pastMatchData = {}
                }
            })
            .catch(e => {
                this.errors.push(e)
            })
    }

}
</script>

<style>
.el-dialog__title {
    font-size: 40px,

}
</style>
