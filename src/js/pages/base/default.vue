<template>
  <div>
      <fish-layout class="home" sider="l">
          <nav slot="header">
            <div class="mobile-menu"> <span class="fa fa-bars"></span> </div>
            <div class="logo">Favorite things</div>
          </nav>
          <side-bar slot="sider"></side-bar>
          <div slot="content">
              <router-view></router-view>
          </div>
      </fish-layout>
  </div>
</template>

<script>
    import sideBar from '../components/sidebar'
    export default {
        components: {
            'side-bar': sideBar
        }
    }
</script>
