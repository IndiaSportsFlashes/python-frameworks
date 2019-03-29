<template>
<div id="matchCreation">
    <el-tabs type="border-card" style="height: 80vh; border: 1px solid #eee ; font-size:15px; font-weight:500;">
        <el-tab-pane label="General">
            <el-form label-width="120px" class="demo-ruleForm">
                <el-container style="font-size:15px; font-weight:500;">
                    <el-main style="border-right: 1px solid #eee; text-align:left">
                        <el-form-item label="Name">
                            <el-input type="textarea" :autosize="{ minRows: 1, maxRows: 4}" placeholder="name" v-model="name" style="width: 500px" clearable>
                            </el-input>
                        </el-form-item>
                        <el-form-item label="Venue">
                            <el-input type="textarea" :autosize="{ minRows: 1, maxRows: 4}" placeholder="venue" v-model="venue" style="width: 500px" clearable>
                            </el-input>
                        </el-form-item>
                        <el-form-item label="Date">
                            <el-date-picker v-model="date" type="datetime" placeholder="Select date and time" default-time="12:00:00">
                            </el-date-picker>
                        </el-form-item>
                        <el-form-item label="Format">
                            <el-checkbox-group v-model="format" :max="1">
                                <el-checkbox label=1>ODI</el-checkbox>
                                <el-checkbox label=2>T20</el-checkbox>
                                <el-checkbox label=3>Test</el-checkbox>
                            </el-checkbox-group>
                        </el-form-item>
                        <el-form label-width="120px" class="demo-ruleForm">
                            <el-form-item label="Country">
                                <el-select v-model="country" value-key="country" placeholder="Select">
                                    <el-option v-for="item in countryData" :key="item.id" :label="item.name" :value="item.id">
                                    </el-option>
                                </el-select>
                            </el-form-item>
                        </el-form>
                    </el-main>
                </el-container>
            </el-form>
        </el-tab-pane>
        <el-tab-pane label="Team">
            <el-form label-width="120px" class="demo-ruleForm">
                <el-container style="font-size:15px; font-weight:500;">
                    <el-main style="border-right: 1px solid #eee; text-align:left">
                        <el-form-item label="Team A">
                            <el-select v-model="team_a" value-key="team_a" v-on:change="OnChangeA" placeholder="Select">
                                <el-option v-for="item in teams" :key="item.id" :label="item.name" :value="item.id" :disabled="item.disabled">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="Squad" v-if=teama_show>
                            <el-table ref="team_a_multipleTable" :data="teamAPlayer" style="width: auto;" height="250" @selection-change="team_a_handleSelectionChange" @click="toggleSelection(values)">
                                <el-table-column type="selection" width="55">
                                </el-table-column>
                                <el-table-column label="Name" width="120">
                                    <template slot-scope="scope">{{ scope.row.name }}</template>
                                </el-table-column>
                            </el-table>
                            <div style="margin-top: 20px">
                                <el-button @click="team_a_toggleSelection()">Clear selection</el-button>
                            </div>
                        </el-form-item>
                    </el-main>
                    <el-main style="text-align:left">
                        <el-form-item label="Team B">
                            <el-select v-model="team_b" value-key="team_b" v-on:change="OnChangeB" placeholder="Select">
                                <el-option v-for="item in teams" :key="item.id" :label="item.name" :value="item.id" :disabled="item.disabled">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="Squad" v-if=teamb_show>
                            <el-table ref="team_b_multipleTable" :data="teamBPlayer" style="width: auto;" height="250" @selection-change="team_b_handleSelectionChange">
                                <el-table-column type="selection" width="55">
                                </el-table-column>
                                <el-table-column label="Name" width="120">
                                    <template slot-scope="scope">{{ scope.row.name }}</template>
                                </el-table-column>
                            </el-table>
                            <div style="margin-top: 20px">
                                <el-button @click="team_b_toggleSelection()">Clear selection</el-button>
                            </div>
                        </el-form-item>
                    </el-main>
                </el-container>
            </el-form>
        </el-tab-pane>
        <el-tab-pane label="Match Type" style="padding:30px">
            <el-form label-width="120px" class="demo-ruleForm">
                <el-form-item >
                    <el-radio v-model="radioType" label="1" @change="OnChangeRadio">Series</el-radio>
                    <el-radio v-model="radioType" label="2" @change="OnChangeRadio">Tournament</el-radio>
                </el-form-item>
                <el-form-item v-if=series_down>
                    <el-select v-model="series" value-key="series" placeholder="Select">
                        <el-option v-for="item in seriesData" :key="item.id" :label="item.name" :value="item.id">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item v-if=tourn_down>
                    <el-select v-model="tournament" value-key="tournament" placeholder="Select">
                        <el-option v-for="item in tournamentData" :key="item.id" :label="item.name" :value="item.id">
                        </el-option>
                    </el-select>
                </el-form-item>
            </el-form>
        </el-tab-pane>
    </el-tabs>
    <div style="border: 2px solid #eee; background-color:#e6e6ff ;padding:15px">
        <!-- <el-button type="info" style="font-size:18px; font-weight:800;">Reset</el-button> -->
        <el-button type="primary" style="font-size:18px; font-weight:800;" @click="submitForm()">Submit</el-button>
    </div>
</div>
</template>

<script>
import match from '../api-services/match.service'
export default {
    name: "matchCreation",
    data() {
        return {
            teama_show: false,
            teamb_show: false,
            series_down: true,
            tourn_down: false,
            name,
            venue: '',
            date: '',
            format: [],
            series: '',
            tournament: '',
            country: '',
            radioType: '1',
            tournamentData: [{
                    "id": 6,
                    "name": "ICC WC 2019"
                },
                {
                    "id": 7,
                    "name": "ICC WC 2015"
                }
            ],
            seriesData: [{
                    "id": 1,
                    "name": "1981-1982 Pakistan v Sri Lanka"
                },
                {
                    "id": 2,
                    "name": "1982 England v India"
                },
                {
                    "id": 3,
                    "name": "1982 England v Pakistan"
                }
            ],
            teams: [{
                    id: 1,
                    name: "Pakistan",
                    status: true
                },
                {
                    id: 2,
                    name: "Sri Lanka",
                    status: true
                },
                {
                    id: 3,
                    name: "India",
                    status: true
                },
                {
                    id: 4,
                    name: "England",
                    status: true
                }
            ],
            countryData: [{
                    "id": 1,
                    "name": "Pakisthan",
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
            teamAPlayer: '',
            teamBPlayer: '',
            team_a_Selection: [],
            team_b_Selection: [],
            team_a: '',
            team_b: '',
            enum_team: {
                1: 'Pakistan',
                2: 'Sri Lanka',
                3: 'India',
                4: 'England'
            }
        };
    },
    created() {
         this.fetchData()
    },
    watch: {
        '$route': 'fetchData'
    },
    methods: {
        fetchData () {
            if (this.$route.params.id) {
            match.getMatch(this.$route.params.id)
                .then(response => {
                    this.name = response.data.data.name
                    this.venue = response.data.data.venue
                    this.date = response.data.data.date
                    this.format.push(response.data.data.format_id.toString())
                    this.team_a = response.data.data.team_a
                    this.team_b = response.data.data.team_b
                    this.teamAPlayer = response.data.data.team_squad_1
                    // this.team_a_toggleSelection(response.data.data.team_squad_1)
                    this.teamBPlayer = response.data.data.team_squad_2
                    this.teama_show = true
                    this.teamb_show = true
                    this.country = response.data.data.country_id;
                    this.series = response.data.data.format_id
                })
                .catch(e => {
                    this.errors.push(e)
                })
            } else {
                this.name = null
                this.venue = null
                this.date = null
                this.format = []
                this.team_a = null
                this.team_b = null
                this.teamAPlayer = null
                // this.team_a_toggleSelection(response.data.data.team_squad_1)
                this.teamBPlayer = null
                this.teama_show = false
                this.teamb_show = false
                this.country = null
                this.series = null
            }
        },
        OnChangeRadio(val) {
            if (val === "1") {
                this.series_down = true;
                this.tourn_down = false;
            } else {
                this.series_down = false;
                this.tourn_down = true;
            }
        },
        team_a_toggleSelection(rows) {
            if (rows) {
                rows.forEach(row => {
                    this.$refs.team_a_multipleTable.toggleRowSelection(row);
                });
            } else {
                this.$refs.team_a_multipleTable.clearSelection();
            }
        },
        team_a_handleSelectionChange(val) {
            this.team_a_Selection = val;
        },
        team_b_toggleSelection(rows) {
            if (rows) {
                rows.forEach(row => {
                    this.$refs.team_b_multipleTable.toggleRowSelection(row);
                });
            } else {
                this.$refs.team_b_multipleTable.clearSelection();
            }
        },
        team_b_handleSelectionChange(val) {
            this.team_b_Selection = val;
        },
        OnChangeA(val) {
            this.teama_show = true
            if (this.enum_team[val] === 'India') {
                this.teamAPlayer = [{
                        "id": 27,
                        "name": "G A Parkar",
                        "team": 3
                    },
                    {
                        "id": 28,
                        "name": "D B Vengsarkar",
                        "team": 3
                    },
                    {
                        "id": 29,
                        "name": "G R Viswanath",
                        "team": 3
                    },
                    {
                        "id": 30,
                        "name": "S M Patil",
                        "team": 3
                    },
                    {
                        "id": 31,
                        "name": "Yashpal Sharma",
                        "team": 3
                    },
                    {
                        "id": 32,
                        "name": "R J Shastri",
                        "team": 3
                    },
                    {
                        "id": 33,
                        "name": "Kapil Dev",
                        "team": 3
                    },
                    {
                        "id": 34,
                        "name": "S M H Kirmani",
                        "team": 3
                    },
                    {
                        "id": 35,
                        "name": "S V Nayak",
                        "team": 3
                    },
                    {
                        "id": 36,
                        "name": "S Madan Lal",
                        "team": 3
                    },
                    {
                        "id": 37,
                        "name": "R G D Willis",
                        "team": 3
                    },
                    {
                        "id": 48,
                        "name": "A Malhotra",
                        "team": 3
                    },
                    {
                        "id": 49,
                        "name": "S M Gavaskar",
                        "team": 3
                    },
                    {
                        "id": 57,
                        "name": "K Srikkanth",
                        "team": 3
                    },
                    {
                        "id": 58,
                        "name": "M Amarnath",
                        "team": 3
                    },
                    {
                        "id": 59,
                        "name": "D R Doshi",
                        "team": 3
                    }
                ]
            } else if (this.enum_team[val] === 'Pakistan') {
                this.teamAPlayer = [{
                        "id": 1,
                        "name": "Mohsin Khan",
                        "team": 1
                    },
                    {
                        "id": 2,
                        "name": "Zaheer Abbas",
                        "team": 1
                    },
                    {
                        "id": 3,
                        "name": "Javed Miandad",
                        "team": 1
                    },
                    {
                        "id": 4,
                        "name": "Haroon Rashid",
                        "team": 1
                    },
                    {
                        "id": 5,
                        "name": "Imran Khan",
                        "team": 1
                    },
                    {
                        "id": 6,
                        "name": "Mansoor Akhtar",
                        "team": 1
                    },
                    {
                        "id": 7,
                        "name": "Ashraf Ali",
                        "team": 1
                    },
                    {
                        "id": 8,
                        "name": "Tahir Naqqash",
                        "team": 1
                    },
                    {
                        "id": 9,
                        "name": "Rashid Khan",
                        "team": 1
                    },
                    {
                        "id": 10,
                        "name": "Sikander Bakht",
                        "team": 1
                    },
                    {
                        "id": 11,
                        "name": "A L F De Mel",
                        "team": 1
                    },
                    {
                        "id": 24,
                        "name": "Wasim Raja",
                        "team": 1
                    },
                    {
                        "id": 25,
                        "name": "Saleem Yousuf",
                        "team": 1
                    },
                    {
                        "id": 26,
                        "name": "Tausif Ahmed",
                        "team": 1
                    },
                    {
                        "id": 50,
                        "name": "Majid Khan",
                        "team": 1
                    },
                    {
                        "id": 51,
                        "name": "Sarfraz Nawaz",
                        "team": 1
                    },
                    {
                        "id": 52,
                        "name": "Wasim Bari",
                        "team": 1
                    },
                    {
                        "id": 53,
                        "name": "Iqbal Qasim",
                        "team": 1
                    },
                    {
                        "id": 63,
                        "name": "Jalaluddin",
                        "team": 1
                    },
                    {
                        "id": 64,
                        "name": "G F Lawson",
                        "team": 1
                    }
                ]
            } else if (this.enum_team[val] === 'Sri Lanka') {
                this.teamAPlayer = [{
                        "id": 23,
                        "name": "G R A de Silva",
                        "team": 2
                    },
                    {
                        "id": 60,
                        "name": "R M H Binny",
                        "team": 2
                    },
                    {
                        "id": 61,
                        "name": "V B John",
                        "team": 2
                    },
                    {
                        "id": 62,
                        "name": "R J Ratnayake",
                        "team": 2
                    }
                ]
            } else if (this.enum_team[val] === 'England') {
                this.teamAPlayer = [{
                        "id": 54,
                        "name": "E E Hemmings",
                        "team": 4
                    },
                    {
                        "id": 55,
                        "name": "D R Pringle",
                        "team": 4
                    },
                    {
                        "id": 56,
                        "name": "M W Gatting",
                        "team": 4
                    }
                ]
            }
        },
        OnChangeB(val) {
            this.teamb_show = true
            if (this.enum_team[val] === 'India') {
                this.teamBPlayer = [{
                        "id": 27,
                        "name": "G A Parkar",
                        "team": 3
                    },
                    {
                        "id": 28,
                        "name": "D B Vengsarkar",
                        "team": 3
                    },
                    {
                        "id": 29,
                        "name": "G R Viswanath",
                        "team": 3
                    },
                    {
                        "id": 30,
                        "name": "S M Patil",
                        "team": 3
                    },
                    {
                        "id": 31,
                        "name": "Yashpal Sharma",
                        "team": 3
                    },
                    {
                        "id": 32,
                        "name": "R J Shastri",
                        "team": 3
                    },
                    {
                        "id": 33,
                        "name": "Kapil Dev",
                        "team": 3
                    },
                    {
                        "id": 34,
                        "name": "S M H Kirmani",
                        "team": 3
                    },
                    {
                        "id": 35,
                        "name": "S V Nayak",
                        "team": 3
                    },
                    {
                        "id": 36,
                        "name": "S Madan Lal",
                        "team": 3
                    },
                    {
                        "id": 37,
                        "name": "R G D Willis",
                        "team": 3
                    },
                    {
                        "id": 48,
                        "name": "A Malhotra",
                        "team": 3
                    },
                    {
                        "id": 49,
                        "name": "S M Gavaskar",
                        "team": 3
                    },
                    {
                        "id": 57,
                        "name": "K Srikkanth",
                        "team": 3
                    },
                    {
                        "id": 58,
                        "name": "M Amarnath",
                        "team": 3
                    },
                    {
                        "id": 59,
                        "name": "D R Doshi",
                        "team": 3
                    }
                ]
            } else if (this.enum_team[val] === 'Pakistan') {
                this.teamBPlayer = [{
                        "id": 1,
                        "name": "Mohsin Khan",
                        "team": 1
                    },
                    {
                        "id": 2,
                        "name": "Zaheer Abbas",
                        "team": 1
                    },
                    {
                        "id": 3,
                        "name": "Javed Miandad",
                        "team": 1
                    },
                    {
                        "id": 4,
                        "name": "Haroon Rashid",
                        "team": 1
                    },
                    {
                        "id": 5,
                        "name": "Imran Khan",
                        "team": 1
                    },
                    {
                        "id": 6,
                        "name": "Mansoor Akhtar",
                        "team": 1
                    },
                    {
                        "id": 7,
                        "name": "Ashraf Ali",
                        "team": 1
                    },
                    {
                        "id": 8,
                        "name": "Tahir Naqqash",
                        "team": 1
                    },
                    {
                        "id": 9,
                        "name": "Rashid Khan",
                        "team": 1
                    },
                    {
                        "id": 10,
                        "name": "Sikander Bakht",
                        "team": 1
                    },
                    {
                        "id": 11,
                        "name": "A L F De Mel",
                        "team": 1
                    },
                    {
                        "id": 24,
                        "name": "Wasim Raja",
                        "team": 1
                    },
                    {
                        "id": 25,
                        "name": "Saleem Yousuf",
                        "team": 1
                    },
                    {
                        "id": 26,
                        "name": "Tausif Ahmed",
                        "team": 1
                    },
                    {
                        "id": 50,
                        "name": "Majid Khan",
                        "team": 1
                    },
                    {
                        "id": 51,
                        "name": "Sarfraz Nawaz",
                        "team": 1
                    },
                    {
                        "id": 52,
                        "name": "Wasim Bari",
                        "team": 1
                    },
                    {
                        "id": 53,
                        "name": "Iqbal Qasim",
                        "team": 1
                    },
                    {
                        "id": 63,
                        "name": "Jalaluddin",
                        "team": 1
                    },
                    {
                        "id": 64,
                        "name": "G F Lawson",
                        "team": 1
                    }
                ]
            } else if (this.enum_team[val] === 'Sri Lanka') {
                this.teamBPlayer = [{
                        "id": 23,
                        "name": "G R A de Silva",
                        "team": 2
                    },
                    {
                        "id": 60,
                        "name": "R M H Binny",
                        "team": 2
                    },
                    {
                        "id": 61,
                        "name": "V B John",
                        "team": 2
                    },
                    {
                        "id": 62,
                        "name": "R J Ratnayake",
                        "team": 2
                    }
                ]
            } else if (this.enum_team[val] === 'England') {
                this.teamBPlayer = [{
                        "id": 54,
                        "name": "E E Hemmings",
                        "team": 4
                    },
                    {
                        "id": 55,
                        "name": "D R Pringle",
                        "team": 4
                    },
                    {
                        "id": 56,
                        "name": "M W Gatting",
                        "team": 4
                    }
                ]
            }
        },
        submitForm() {
            let obj = {}
            obj.name = this.name
            obj.venue = this.venue
            obj.date = null
            obj.format = parseInt(this.format[0])
            if (this.radioType === "1") {

                obj.match_type = this.series
            } else {
                obj.match_type = this.tournament
            }
            obj.country = this.country
            let teamSquadA = [], teamSquadB = [];
            this.team_a_Selection.forEach(function(player){
                teamSquadA.push({
                    player: player.id,
                    team: player.team,
                    status: true
                })
            })
            this.team_b_Selection.forEach(function(player){
                teamSquadB.push({
                    player: player.id,
                    team: player.team,
                    status: true
                })
            })
            obj.team_squad_1 = teamSquadA
            obj.team_squad_2 = teamSquadB
            obj.team_a = this.team_a
            obj.team_b = this.team_b
            obj.match_status = 'UPCOMING'
            match.matchCreation (obj)
                .then(response => {
                    this.$notify({
                                title: 'Success',
                                message: 'Match Created Successfully',
                                type: 'success'
                            });
                    this.$router.replace({ name: "MatchList" });
                })
            .catch(e => {
            this.errors.push(e)
            })
            }
    }
}
</script>
