import VueCookie from 'vue-cookie'

export const middleware = (middleware) => (to, from, next) => {
    middleware(to, from, next)
}

export const guest = (to, from, next) => {
    if (VueCookie.get('_uat')) {
        next({name: 'things.list'})
    } else {
        next()
    }
}

// Middleware for all auth-protected routes
export const auth = (to, from, next) => {
    if (!VueCookie.get('_uat')) {
        next({name: 'things.home'})
    } else {
        next()
    }
}
