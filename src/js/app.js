import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import routes from './routes';
import VueCookie from 'vue-cookie';
import moment from 'moment';
import http from './helpers/http';
import FishUI from 'fish-ui'
import store from './store/index';

Vue.use(VueRouter);
Vue.use(VueCookie);
Vue.use(FishUI)

const router = new VueRouter({
	routes:routes,
    mode: 'history'
});

Vue.mixin({
    data () {
        return {
            http: http
        }
    }
})

const vm = new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
});

export default vm
