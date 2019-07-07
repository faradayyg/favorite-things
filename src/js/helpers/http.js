import axios from 'axios';
import VueCookie from 'vue-cookie';
import store from '@/store/index.js';

let headers = {},
    running = 0;
export const config = {
    "cookie_name": '_uat',
    // "base_url": 'http://localhost:8000/api'
    "base_url": '/api'

}
headers['Authorization'] = 'Bearer ' + VueCookie.get(config.cookie_name);
headers['Accept'] = 'application/json';

const http = {
  axios: axios.create({baseURL: config.base_url, headers: headers}),
  send(type, args) {
    if (!running) {
      store.commit('setAjaxStatus', false)
    }
    running++;
    const respond = (func, resp) => {
      running--;
      if (!running) {
       store.commit('setAjaxStatus', true)
      }
      if (!resp) {
        resp = {};
      }
      func(resp.data, resp.headers, resp.status);
    };
    return new Promise(function (resolve, reject) {
      this[type]
        .apply(this, args)
        .then(resp => {
          respond(resolve, resp);
        })
        .catch((error) => {
          let resp = error.response;
          if (resp && resp.hasOwnProperty('status')) {
              if(resp.status && resp.status == 401)
              {
                VueCookie.delete(config.cookie_name);
              }
              else if(resp.status == 422)
              {
                window.location.reload();
              }
              else if(resp.status == 425)
              {
                window.location.replace('/verify/');
              }
          }
          respond(reject, resp);
        });
    }.bind(this.axios));
  },
  get() {
    return this.send('get', arguments);
  },
  post() {
    return this.send('post', arguments);
  },
  put() {
    return this.send('put', arguments);
  },
  patch() {
    return this.send('patch', arguments);
  },
  delete() {
    return this.send('delete', arguments);
  },
  getHeaders() {
    return headers;
  },
  getHeader(name){
    return headers[name];
  },
  headerIs(name, value) {
    return headers[name] == value;
  },
  setHeaders(new_headers) {
    headers = new_headers;
    return this.renew();
  },
  setHeader(name, value, norenew) {
    headers[name] = value;
    if (!norenew) this.renew();
    return this;
  },
  removeHeader(name, norenew) {
    delete headers[name];
    if (!norenew) this.renew();
    return this;
  },
  renew() {
    this.axios = axios.create({baseURL: process.env.API_BASE_URL, headers: headers});
    return this;
  }
};

export default http;
