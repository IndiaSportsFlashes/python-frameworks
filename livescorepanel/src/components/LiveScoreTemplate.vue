<template>
<div id="panel">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
        <el-tabs type="border-card" style="height: 75vh; border: 1px solid #eee ; font-size:15px; font-weight:500;">
            <el-tab-pane label="Bowling">
                <el-container style="font-size:15px; font-weight:500;">
                    <el-main style="text-align:left">
                        <el-form-item label="Current Bowler" prop="cur_bowler">
                            <el-select v-model="ruleForm.cur_bowler" value-key="ruleForm.cur_bowler" placeholder="Select">
                                <el-option v-for="item in bowling_players" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="Ball Type" prop="ball_type">
                            <el-select v-model="ruleForm.ball_type" placeholder="Select">
                                <el-option v-for="item in balltype" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item prop="bowling_checkList">
                            <el-checkbox-group v-model="ruleForm.bowling_checkList" :max="1">
                                <el-checkbox label="Byes"></el-checkbox>
                                <el-checkbox label="Leg Byes"></el-checkbox>
                                <el-checkbox label="Wide"></el-checkbox>
                                <el-checkbox label="No Ball"></el-checkbox>
                                <el-checkbox label="Penalty"></el-checkbox>
                            </el-checkbox-group>
                        </el-form-item>
                    </el-main>
                </el-container>
            </el-tab-pane>
            <el-tab-pane label="Batting">
                <el-container style="font-size:15px; font-weight:500;">
                    <el-main style="border-right: 1px solid #eee; text-align:left">
                        <el-form-item label="striker" prop="striker">
                            <el-select v-model="ruleForm.striker" value-key="ruleForm.striker" placeholder="Select">
                                <el-option v-for="item in batting_players" :key="item.id" :label="item.name" :value="item.id" :disabled="item.disabled">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="Strike Position" prop="striker_position">
                            <el-input-number v-model="ruleForm.striker_position" :min="1" :max="11"></el-input-number>
                        </el-form-item>
                        <el-form-item label="Run" prop="striker_score">
                            <el-input-number v-model="ruleForm.striker_score" :min="0" :max="6"></el-input-number>
                        </el-form-item>
                        <el-form-item prop="striker_4_6">
                            <el-checkbox-group v-model="ruleForm.striker_4_6" :max="1">
                                <el-checkbox label="striker 4'"></el-checkbox>
                                <el-checkbox label="striker 6'"></el-checkbox>
                            </el-checkbox-group>
                        </el-form-item>
                        <el-form-item label="Shot Type" prop="shot_type">
                            <el-select v-model="ruleForm.shot_type" placeholder="Select">
                                <el-option v-for="item in shottype" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="striker Out" prop="striker_out">
                            <el-select v-model="ruleForm.striker_out" placeholder="Select">
                                <el-option v-for="item in out" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="striker Wicket" prop="striker_wicket">
                            <el-select v-model="ruleForm.striker_wicket" value-key="striker_wicket" placeholder="Select">
                                <el-option v-for="item in bowling_players" :key="item.id" :label="item.name" :value="item.id" :disabled="item.disabled">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="Field Player" prop="field_player">
                            <el-select v-model="ruleForm.field_player" placeholder="Select">
                                <el-option v-for="item in bowling_players" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                    </el-main>
                    <el-main style="text-align:left">
                        <el-form-item label="Non striker" prop="non_striker">
                            <el-select v-model="ruleForm.non_striker" value-key="ruleForm.non_striker" placeholder="Select">
                                <el-option v-for="item in batting_players" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="Non Striker Position" prop="non_striker_position">
                            <el-input-number v-model="ruleForm.non_striker_position" :min="1" :max="11"></el-input-number>
                        </el-form-item>
                        <el-form-item label="Non striker Out" prop="non_striker_out">
                            <el-select v-model="ruleForm.non_striker_out" placeholder="Select">
                                <el-option v-for="item in out" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="Non striker Wicket" prop="non_striker_wicket">
                            <el-select v-model="ruleForm.non_striker_wicket" placeholder="Select">
                                <el-option v-for="item in bowling_players" :key="item.id" :label="item.name" :value="item.id">
                                </el-option>
                            </el-select>
                        </el-form-item>
                    </el-main>
                </el-container>
            </el-tab-pane>
            <el-tab-pane label="Teams" style="padding:30px">
                <el-container>
                    <el-header style="text-align: center; font-size: 20px ;border-bottom: 2px solid #eee ;padding:15px">
                        <span style="margin-right:40px">Target : {{this.card.team_a_target}}</span>
                        <el-radio-group v-model="innings" v-on:change="onChageInnings">
                            <el-radio :label="1">INNINGS 1</el-radio>
                            <el-radio :label="2">INNINGS 2</el-radio>
                        </el-radio-group>
                    </el-header>
                    <el-main>
                        <el-table :data="teamData" align="center">
                            <el-table-column prop="team_a" :label=team_a_name width="180">
                            </el-table-column>
                            <el-table-column prop="team_b" :label=team_b_name width="180">
                            </el-table-column>
                        </el-table>
                    </el-main>
                </el-container>
            </el-tab-pane>
            <el-tab-pane label="Comment" style="padding:30px">
                <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
            </el-tab-pane>
        </el-tabs>
        <div style="border: 2px solid #eee; background-color:#e6e6ff ;padding:15px">
            <!-- <el-button type="info" style="font-size:18px; font-weight:800;">Previous</el-button> -->
            <el-button type="primary" style="font-size:18px; font-weight:800;" @click="submitForm('ruleForm')">Submit</el-button>
            <el-button @click="resetForm('ruleForm')" style="font-size:18px; font-weight:800;">Reset</el-button>
            <el-button type="danger" style="font-size:18px; font-weight:800;" @click="endMatch('ruleForm')">End Match</el-button>
        </div>
    </el-form>
</div>
</template>

<script>
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import livescore from '../api-services/livescore.service'
import result from '../api-services/result.service'

export default {
    name: 'panel',
    data() {
        return {
            bowling_players: [],
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
            batting_players: [],
            out: [{
                    "id": 1,
                    "name": "LBW",
                    "status": true
                },
                {
                    "id": 2,
                    "name": "Bowled",
                    "status": true
                },
                {
                    "id": 3,
                    "name": "Caught",
                    "status": true
                }
            ],
            shottype: [{
                    "id": 1,
                    "name": "Drive",
                    "status": true
                },
                {
                    "id": 2,
                    "name": "Pull",
                    "status": true
                },
                {
                    "id": 3,
                    "name": "Upper Cut",
                    "status": true
                }
            ],
            balltype: [{
                    "id": 1,
                    "name": "Short",
                    "status": true
                },
                {
                    "id": 2,
                    "name": "Fuller",
                    "status": true
                },
                {
                    "id": 3,
                    "name": "Good",
                    "status": true
                }
            ],

            editor: ClassicEditor,
            editorData: '<p>Content of the editor.</p>',
            editorConfig: {
                // The configuration of the editor.
            },
            card: {
                "striker": 0,
                "striker_position": 0,
                "striker_run": 0,
                "striker_4": 0,
                "striker_6": 0,
                "striker_strikerate": 0,
                "striker_balls": 0,
                "striker_out": null,
                "field_player": null,
                "striker_wicket": null,
                "non_striker": 0,
                "non_striker_position": 0,
                "non_striker_run": 0,
                "non_striker_4": 0,
                "non_striker_6": 0,
                "non_striker_strikerate": 0,
                "non_striker_balls": 0,
                "non_striker_out": null,
                "non_striker_wicket": null,
                "cur_bowler": 0,
                "cur_bowler_over": 0,
                "cur_bowler_eco": 0,
                "cur_bowler_mai": 0,
                "cur_bowler_wic": 0,
                "cur_bowler_run": 0,
                "team_a_score": 0,
                "team_a_over": 0,
                "team_a_wicket": 0,
                "team_a_target": 0,
                "team_b_score": 0,
                "team_b_over": 0,
                "team_b_wicket": 0,
                "team_b_target": 0,
                "byes": 0,
                "leg_byes": 0,
                "wide": 0,
                "no_ball": 0,
                "pnlt": 0,
                "ball_type": 0,
                "shot_type": 0,
                "run_scored": 0,
                "innings": 1,
                "created": null,
                "modified": null,
                "cur_bowler_spell": 0,
                "prv_bowler": null,
                "prv_bowler_over": 0,
                "prv_bowler_eco": 0,
                "prv_bowler_mai": 0,
                "prv_bowler_wic": 0,
                "prv_bowler_spell": 0,
                "prv_bowler_run": 0,
                "comment": "some Comment"
            },
            currentRunRate: '',
            data: {},
            innings: 1,
            team_a_name: '',
            team_b_name: '',
            teamData: [{
                team_a: '',
                team_b: ''
            }, {
                team_a: '',
                team_b: ''
            }, {
                team_a: '',
                team_b: ''
            }],
            ruleForm: {
                cur_bowler: '',
                striker: '',
                non_striker: '',
                striker_position: '',
                non_striker_position: '',
                ball_type: '',
                shot_type: '',
                striker_out: null,
                striker_wicket: null,
                field_player: null,
                non_striker_out: null,
                non_striker_wicket: null,
                bowling_checkList: [],
                striker_4_6: [],
                striker_score: 0
            },
            rules: {
                cur_bowler: [{
                    required: true,
                    message: 'Please enter Current Bowler',
                    trigger: 'change'
                }],
                striker: [{
                    required: true,
                    message: 'Please enter Striker',
                    trigger: 'change'
                }],
                non_striker: [{
                    required: true,
                    message: 'Please enter Non Striker',
                    trigger: 'change'
                }],
                ball_type: [{
                    required: true,
                    message: 'Please enter Ball Type',
                    trigger: 'change'
                }],
                shot_type: [{
                    required: true,
                    message: 'Please enter shot Type',
                    trigger: 'change'
                }]
            }
        };
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    if (this.ruleForm.striker_score > 0) {
                        this.card.striker_run = this.card.striker_run + this.ruleForm.striker_score
                        this.card.cur_bowler_run = this.card.cur_bowler_run + this.ruleForm.striker_score
                        this.card.run_scored = this.ruleForm.striker_score
                    } else if (this.ruleForm.striker_4_6.length > 0) {
                        if (this.ruleForm.striker_4_6[0] == "striker 4'") {
                            this.card.striker_run = this.card.striker_run + 4
                            this.card.striker_4 = this.card.striker_4 + 1
                            this.card.cur_bowler_run = this.card.cur_bowler_run + 4
                            this.card.run_scored = 4
                        } else {
                            this.card.striker_run = this.card.striker_run + 6
                            this.card.cur_bowler_run = this.card.cur_bowler_run + 6
                            this.card.striker_6 = this.card.striker_6 + 1
                            this.card.run_scored = 6
                        }
                    }
                    this.card.team_a_over = this.card.cur_bowler_over
                    if (this.card.cur_bowler_over % 1 == 0.6) {
                        this.card.cur_bowler_over = Math.trunc(this.card.cur_bowler_over) + 1.1
                    } else {
                        this.card.cur_bowler_over = (this.card.cur_bowler_over + 0.1).toFixed(1)
                    }
                    if (this.card.team_a_over % 1 == 0.6) {
                        this.innings == 1 ? this.card.team_a_over = Math.trunc(this.card.team_a_over) + 1.1 : this.card.team_b_over = Math.trunc(this.card.team_b_over) + 1.1
                    } else {
                        this.innings == 1 ? this.card.team_a_over = (this.card.team_a_over + 0.1).toFixed(1) : this.card.team_b_over = (this.card.team_b_over + 0.1).toFixed(1)
                    }
                    this.innings == 1 ? this.card.team_a_score = this.card.team_a_score + this.card.run_scored : this.card.team_b_score = this.card.team_b_score + this.card.run_scored
                    this.innings == 1 ? this.card.team_a_target = this.card.team_a_target + this.card.run_scored : this.card.team_b_target = this.card.team_a_target - (this.card.team_b_target + this.card.run_scored)
                    let cur_bowler_bowl = Math.trunc(this.card.cur_bowler_over) * 6 + (this.card.cur_bowler_over % 1) * 10
                    this.card.cur_bowler_eco = (this.card.cur_bowler_run / cur_bowler_bowl).toFixed(3) * 10
                    this.card.striker_balls = this.card.striker_balls + 1
                    this.card.striker_strikerate = (this.card.striker_run / (this.card.striker_balls)).toFixed(4) * 100
                    if (this.ruleForm.striker_out || this.ruleForm.non_striker_out) {
                        this.card.cur_bowler_wic = this.card.cur_bowler_wic + 1
                        if (this.innings == 1) {
                            this.card.team_a_wicket = this.card.team_a_wicket + 1
                        } else if (this.innings == 2) {
                            this.card.team_b_wicket = this.card.team_b_wicket + 1
                        }
                    }
                    if (this.ruleForm.bowling_checkList.length > 0) {
                        if (this.ruleForm.bowling_checkList[0] == 'Byes')
                            this.card.byes = this.card.byes + 1
                        if (this.ruleForm.bowling_checkList[0] == 'Leg Byes')
                            this.card.leg_byes = this.card.leg_byes + 1
                        if (this.ruleForm.bowling_checkList[0] == 'Wide')
                            this.card.wide = this.card.wide + 1
                        if (this.ruleForm.bowling_checkList[0] == 'No Ball')
                            this.card.no_ball = this.card.no_ball + 1
                        if (this.ruleForm.bowling_checkList[0] == 'Penalty')
                            this.card.pnlt = this.card.pnlt + 1
                    }
                    this.card.striker = this.ruleForm.striker
                    this.card.striker_position = this.ruleForm.striker_position
                    this.card.non_striker_position = this.ruleForm.non_striker_position
                    this.card.striker_wicket = this.ruleForm.striker_wicket
                    this.card.striker_out = this.ruleForm.striker_out
                    this.card.non_striker = this.ruleForm.non_striker
                    this.card.non_striker_wicket = this.ruleForm.non_striker_wicket
                    this.card.non_striker_out = this.ruleForm.non_striker_out
                    this.card.cur_bowler = this.ruleForm.cur_bowler
                    this.card.field_player = this.ruleForm.field_player
                    this.card.ball_type = this.ruleForm.ball_type
                    this.card.shot_type = this.ruleForm.shot_type
                    this.card.innings = this.innings
                    this.card.modified = this.card.created = new Date()
                    delete this.card.id;
                    livescore.postLiveMatch(this.card)
                        .then(response => {
                            this.$refs[formName].resetFields();
                            this.data = response.data
                            this.autoFillData(this.data)
                            this.$notify({
                                title: 'Success',
                                message: 'Score Updated Successfully',
                                type: 'success'
                            });
                        })
                        .catch(e => {
                            console.log(e)
                        })
                } else {
                    this.$notify.error({
                        title: 'Error',
                        message: 'Please Enter All Required Field'
                    });
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
            this.autoFillData(this.data)

        },
        endMatch(formName) {
            let team = this.$store.state.scoreCard.team_a_score > this.$store.state.scoreCard.team_b_score ? this.$store.state.scoreCard.team_a : this.$store.state.scoreCard.team_b
            let runs = (team == this.$store.state.scoreCard.team_a) ? (this.$store.state.scoreCard.team_a_score - this.$store.state.scoreCard.team_b_score) : this.$store.state.scoreCard.team_b_score - this.$store.state.scoreCard.team_a_score
            let wickets = (team == this.$store.state.scoreCard.team_a) ? (11 - this.$store.state.scoreCard.team_a_wicket) : (11 - this.$store.state.scoreCard.team_b_wicket)
            let payload = {
                "match_id": this.$store.state.scoreCard.match_id,
                "team": team,
                "runs": runs,
                "wickets": wickets
            }
            result.endMatch(payload)
                .then(response => {
                    this.$notify({
                        title: 'Success',
                        message: 'Match Ended Successfully',
                        type: 'success'
                    });
                    this.$router.replace({
                        name: "MatchList"
                    });
                })
                .catch(e => {
                    console.log(e)
                })
        },
        autoFillData(data) {
            let scoreCardHeader = {};
            let currentRun, battingTeam, runs, wickets, over, strikerName, nonstrikerName, key, curBowlerName, preBowlerName, playersName;
            if (data.card) {
                this.card = data.card
                this.ruleForm.striker = this.card.striker
                this.ruleForm.non_striker = this.card.non_striker
                this.ruleForm.cur_bowler = this.card.cur_bowler
                this.ruleForm.striker_position = this.card.striker_position
                this.ruleForm.non_striker_position = this.card.non_striker_position
                this.teamData[0]['team_a'] = "Team Total : " + this.card.team_a_score
                this.teamData[0]['team_b'] = "Team Total : " + this.card.team_b_score
                this.teamData[1]['team_a'] = "Team Over : " + this.card.team_a_over
                this.teamData[1]['team_b'] = "Team Over : " + this.card.team_b_over
                this.teamData[2]['team_a'] = "Team Wicket : " + this.card.team_a_wicket
                this.teamData[2]['team_b'] = "Team Wicket : " + this.card.team_b_wicket
                this.innings = this.card.innings
                if (this.card.innings == 1) {
                    this.batting_players = this.getPlayers(this.team_enum[this.$route.query.team_a])
                    this.bowling_players = this.getPlayers(this.team_enum[this.$route.query.team_b])
                    currentRun = Math.trunc(this.card.team_a_over) * 6 + (this.card.team_a_over % 1) * 10
                    this.currentRunRate = Math.round(this.card.team_a_score / currentRun)
                    runs = this.card.team_a_score
                    wickets = this.card.team_a_wicket
                    over = this.card.team_a_over
                    battingTeam = this.team_enum[this.$route.query.team_a]
                } else {
                    this.bowling_players = this.getPlayers(this.team_enum[this.$route.query.team_a])
                    this.batting_players = this.getPlayers(this.team_enum[this.$route.query.team_b])
                    currentRun = Math.trunc(this.card.team_b_over) * 6 + (this.card.team_b_over % 1) * 10
                    this.currentRunRate = Math.round(this.card.team_b_score / currentRun)
                    runs = this.card.team_b_score
                    wickets = this.card.team_b_wicket
                    over = this.card.team_b_over
                    battingTeam = this.team_enum[this.$route.query.team_b]
                }
                for (key in this.batting_players) {
                    if (this.batting_players[key]['id'] == this.card.striker) {
                        strikerName = this.batting_players[key]['name']
                    }
                    if (this.batting_players[key]['id'] == this.card.non_striker) {
                        nonstrikerName = this.batting_players[key]['name']
                    }
                }
                for (key in this.bowling_players) {
                    if (this.bowling_players[key]['id'] == this.card.cur_bowler) {
                        curBowlerName = this.bowling_players[key]['name']
                    }
                    if (this.bowling_players[key]['id'] == this.card.prv_bowler) {
                        preBowlerName = this.bowling_players[key]['name']
                    }
                }
                scoreCardHeader = {
                    "currentRunRate": this.currentRunRate,
                    "runs": runs,
                    "wickets": wickets,
                    "over": over,
                    "battingTeam": battingTeam
                }
                playersName = {
                    "strikerName": strikerName,
                    "nonstrikerName": nonstrikerName,
                    "curBowlerName": curBowlerName,
                    "preBowlerName": preBowlerName
                }
                this.$store.commit('addScoreCard', this.card)
                this.$store.commit('addScoreCardHeader', scoreCardHeader)
                this.$store.commit('addPlayersName', playersName)
                this.$store.commit('changeShowScoreCard', true)
            } else {
                this.card['match_id'] = this.$route.params.id
                this.card['team_a'] = this.$route.query.team_a
                this.card['team_b'] = this.$route.query.team_b
                this.batting_players = this.getPlayers(this.team_enum[this.$route.query.team_a])
                this.bowling_players = this.getPlayers(this.team_enum[this.$route.query.team_b])
                this.$store.commit('changeShowScoreCard', false)

            }
        },
        getPlayers(team) {
            if (team == "Pakistan") {
                return [{
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
            } else if (team == 'Sri Lanka') {
                return [{
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
            } else if (team == 'India') {
                return [{
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
            } else if (team == 'England') {
                return [{
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
        onChageInnings() {
            this.ruleForm.striker = 'select'
            this.ruleForm.non_striker = 'select'
            this.ruleForm.cur_bowler = 'select'
            this.ruleForm.striker_position = ''
            this.ruleForm.non_striker_position = ''
            if (this.innings == 1) {
                this.batting_players = this.getPlayers(this.team_enum[this.$route.query.team_a])
                this.bowling_players = this.getPlayers(this.team_enum[this.$route.query.team_b])
            } else {
                this.bowling_players = this.getPlayers(this.team_enum[this.$route.query.team_a])
                this.batting_players = this.getPlayers(this.team_enum[this.$route.query.team_b])
            }
        }
    },
    created() {
        livescore.getLiveMatch(this.$route.params.id)
            .then(response => {
                this.team_a_name = this.team_enum[this.$route.query.team_a]
                this.team_b_name = this.team_enum[this.$route.query.team_b]
                this.data = response.data
                this.autoFillData(this.data)
            })
            .catch(e => {
                console.log(e)
            })

    }
}
</script>
