<template>
    <div>
        <things-list-component :url="url" />
    </div>
</template>

<script>
    import ThingsListComponent from '@/pages/components/ThingsListComponent'
    export default {
        components: {
            ThingsListComponent
        },
        data () {
            return {
                url: '/things/'
            }
        }
    }
</script>
