import vm from '@/app.js'
import VueCookie from 'vue-cookie'
import {config} from '@/helpers/http'

export const logout = ({ state }) => {
  vm.http.setHeader('Authorization', null)
  VueCookie.delete('_uat')
  VueCookie.delete('_urt')
  window.localStorage.clear()
  window.location.reload()
}

export const login = ({commit, state}, userData) => {
    window.localStorage.setItem('userData', userData)
    VueCookie.set('_uat', userData['access'])
    VueCookie.set('_urt', userData['refresh'])
    vm.http.setHeader('Authorization', `Bearer ${userData['access']}`)
    commit('setUserData', userData)
}

export const fetchCategories = ({commit, state}) => {
    fetch(`${config.base_url}/things/categories/`).then(resp => resp.json()).then(data => {
        commit('setCategories', data)
    })
}
