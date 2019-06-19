import vm from '@/app.js'

export const logout = ({ state }) => {
  vm.$http.setHeader('Authorization', null)
  vm.$cookie.delete('_uat')
  window.localStorage.clear()
  window.location.reload()
}