export const setUserData = (state, userToken) => {
  state.userToken = userToken['access']
  state.refreshToken = userToken['refresh']
}

export const setCategories = (state, categories) => {
    state.categories = categories
}
