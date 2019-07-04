import Default from './pages/base/default'
import ThingsList from './pages/ThingList'
import notFound from './pages/404'
import Login from './pages/Login'
import Logout from './pages/Logout'
import CategoriesList from './pages/CategoriesList'
import CategoryThingsList from './pages/CategoryThingsList'
import {middleware, guest, auth} from './helpers/middleware'

export default [
    {
        path: '',
        component: Login,
        beforeEnter: middleware(guest),
        name: 'things.home'
    },
    {
        path: '/logout',
        component: Logout,
        beforeEnter: middleware(auth),
        name: 'things.logout'
    },
    {
        path: '/favourite-things',
        component: Default,
        beforeEnter: middleware(auth),
        children: [
            {
                path: '/',
                component: ThingsList,
                name: 'things.list'

            },
            {
                path: '/categories',
                component: CategoriesList,
                name: 'things.categories'
            },
            {
                path: '/categories/:id',
                component: CategoryThingsList,
                name: 'things.category.items',
                props: true
            },
            {
                path: '*',
                component: notFound
            }
        ]
    },
    {
        path: '*',
        component: notFound,
    }
]
