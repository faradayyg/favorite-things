import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import routes from './routes';
import VueCookie from 'vue-cookie';
import moment from 'moment';
import http from './helpers/http';
import FishUI from 'fish-ui'
import store from './store/index';
import {vueTopprogress} from "vue-top-progress";
import swal from 'sweetalert';

Vue.use(VueRouter);
Vue.use(VueCookie);
Vue.use(vueTopprogress);
Vue.use(FishUI);

const router = new VueRouter({
	routes:routes,
    mode: 'history'
});

Vue.mixin({
    data () {
        return {
            http,
            swal
        }
    },
    methods: {
        confirmDialog(text = 'Are You Sure?', heading = 'Sure?', buttonText = ['No', 'Yes']) {
            return new Promise ((resolve, reject) => {
                swal({
                    title: heading,
                    text: text,
                    buttons: buttonText
                }).then(e => {
                    if (e) {
                        resolve(e)
                    } else {
                        reject(e)
                    }
                })
            });
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
