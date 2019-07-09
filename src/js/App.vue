<template>
  <div id="app">
    <vue-topprogress ref='topProgress' color='#f00'/>
    <router-view></router-view>
  </div>
</template>

<script>
import '@css/custom.css' 
import {mapState} from 'vuex';
import {vueTopprogress} from "vue-top-progress";

export default {
  name: 'app',
  components: {
  	vueTopprogress
  },
  computed: {
  	...mapState(['makingNetworkCall'])
  },
  watch: {
  	makingNetworkCall (oldValue, newValue) {
  		if (newValue == true) {
  			this.$refs.topProgress.start()
  		} else {
  			this.$refs.topProgress.done()
  		}
  	}
  }
}
</script>
