<template>
    <fish-menu @change="sidebarClicked" mode="inline" style="width: 200px;">
     <template v-for="(link, index) in links">
         <fish-option :index="index+1" :content="link.text"></fish-option>
     </template>
    </fish-menu>
</template>

<script>
    import links from './sidebar-links'
    export default {
        data () {
            return {
                links: links
            }
        },
        methods: {
            sidebarClicked (index) {
                this.$router.push(this.links[index-1]['link'])
            }
        },
        mounted: () => {
        }
    }
</script>