<template>
<el-table stripe :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))" style="height: 70vh; border: 8px solid #eee ; font-size:15px; font-weight:500; width: auto padding:20px" class="livematchlist">
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
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">Open</el-button>
        </template>
    </el-table-column>
</el-table>
</template>

<script>
import match from '../api-services/match.service'

export default {
    name: "livematchlist",
    data() {
        return {
            tableData: [],
            search: '',
            team_enum: {
                1: 'Pakistan',
                2: 'Sri Lanka',
                3: 'India',
                4: 'England'
            },
        }
    },
    methods: {
        handleEdit(index, row) {
            this.$router.replace({
                name: "LiveScorePanel",
                params: {
                    id: row['id']
                },
                query: {
                    team_a: row['team_a'],
                    team_b: row['team_b']
                }
            })
        }
    },
    created() {
        match.getMatchList("LIVE")
            .then(response => {
                let data = response.data.data
                let match
                let matchData = {}
                for (match in data) {
                    matchData['id'] = data[match]['id']
                    matchData['name'] = data[match]['name']
                    matchData['date'] = data[match]['date']
                    matchData['venue'] = data[match]['venue']
                    matchData['country'] = this.team_enum[data[match]['country_id']]
                    matchData['toss'] = this.team_enum[data[match]['toss']]
                    matchData['team_a'] = data[match]['team_a']
                    matchData['team_b'] = data[match]['team_b']
                    this.tableData.push(matchData)
                    matchData = {}
                }
            })
            .catch(e => {
                this.errors.push(e)
            })
    }

}
</script>
