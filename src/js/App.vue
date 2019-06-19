<template>
  <div id="app">
    <vue-topprogress ref="topProgress"></vue-topprogress>
    <router-view></router-view>
  </div>
</template>

<script>
import { vueTopprogress } from 'vue-top-progress';

export default {
  name: 'app',
  components:{
    vueTopprogress
  },
  methods:
  {
    hideLoading () {
      this.$refs.topProgress.done();
    },
    showLoading () {
       this.$refs.topProgress.start()
    }
  },
  mounted(){},
  beforeDestroy(){}
}
</script>
