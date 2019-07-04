<template>
	<div>
		<things-list-component :url="url" />
	</div>
</template>

<script>
	import ThingsListComponent from '@/pages/components/ThingsListComponent'
	export default {
		props: ['id'],
		components: {
			ThingsListComponent
		},
		computed: {

		},
		data () {
			return {
				url: `/things/categories/${this.id}/items/`,
			}
		},
	}
</script>