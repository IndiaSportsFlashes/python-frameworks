import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    scoreCard : {},
    scoreCardHeader : {},
    playersName:{},
    showScoreCard:false
  },
  mutations: {
    addScoreCard(state, scoreCard) {
      state.scoreCard = scoreCard
    },
    addScoreCardHeader(state, scoreCardHeader) {
      state.scoreCardHeader = scoreCardHeader
    },
    addPlayersName(state, playersName) {
      state.playersName = playersName
    },
    changeShowScoreCard(state, showScoreCard) {
      state.showScoreCard = showScoreCard
    }
  },
  getters: {
    scoreCard: state => state.scoreCard,
    scoreCardHeader : state => state.scoreCardHeader,
    playersName : state => state.playersName,
    showScoreCard : state => state.showScoreCard


  }
})
