import Vue from 'vue'
import Router from 'vue-router'
import LiveMatchList from '../components/LiveMatchList'
import LiveScorePanel from '../components/LiveScorePanel'
import MatchList from '../components/MatchList'
import MatchCreation from '../components/MatchCreation'




Vue.use(Router)

let routes = [
  {
    path: '/livematchlist',
    name: 'LiveMatchList',
    component: LiveMatchList
  },
  {
    path: '/livescorepanel/:id',
    name: 'LiveScorePanel',
    component: LiveScorePanel
  },
  {
    path: '/matchlist',
    name: 'MatchList',
    component: MatchList
  },
  {
    path: '/matchcreation',
    name: 'MatchCreation',
    component: MatchCreation
  },
  {
    path: '/matchedit/:id',
    name: 'MatchEdit',
    component: MatchCreation
  }
]


export default new Router({
  mode: 'history',
  routes
})
