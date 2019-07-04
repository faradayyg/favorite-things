<template>
  <div>
      <fish-layout class="home" sider="l">
          <nav slot="header">
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

<style>
  .fish.layout.home > .header {
    padding: 0;
    background: #e0f0fa;
  }
  .fish.layout.home .has-sider > .content {
    margin: 20px;
    padding: 0.7em 1em;
  }
  .fish.layout.home .logo {
    padding: 1em;
  }
  .logo {
    padding: 0.7em .8em;
    font-weight: bold;
    font-size: 1.2rem;
  }
</style>
