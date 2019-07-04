<template>
    <div>
        <h1>Logging out...</h1>
    </div>
</template>

<script>
    import {mapActions} from 'vuex'

    export default {
        methods: {
            ...mapActions([
                'logout'
            ])
        },
        mounted () {
            this.logout()
        }
    }
</script>
