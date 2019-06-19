import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import routes from './routes';
import VueCookie from 'vue-cookie';
import swal from 'sweetalert';
import moment from 'moment';
import http from './helpers/http';
import VeeValidate from 'vee-validate';
import store from './store/index';
Vue.use(VueRouter);
Vue.use(VueCookie);
Vue.use(VeeValidate);

const router = new VueRouter({
	routes:routes,
    mode: 'history'
});

const vm = new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
});

export default vm
