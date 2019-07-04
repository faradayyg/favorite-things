<template>
	<div>
		<fish-button type="positive" @click="showModalFunction"><i class="fa fa-search"></i> Add Item</fish-button>
		<fish-table :columns="tableColumns" noMoreText="No Favourite thing found" :data="thingsList"></fish-table>

		<!--    Modal to add or edit favourite thing    -->
        <fish-modal :title=" ((isEditing == false) ? 'Add new' : 'Edit') + ' favourite thing'" :visible.sync="showModal">
          <fish-form>
              <fish-field label="Name">
                <fish-input v-model="newData.title"></fish-input>
              </fish-field>
              <fish-field label="category">
                <fish-select search v-if="categories.length > 0" v-model="newData.category_id" :value="newData.category_id">
                    <fish-option :index="category.id" :value="category.id" v-for="(category, index) in categories" :content="category.name"></fish-option>
                </fish-select>
              </fish-field>
            <fish-field label="Description">
              <fish-input type="textarea" v-model="newData.description"></fish-input>
            </fish-field>
            <fish-field label="Ranking">
              <fish-input type="number" v-model="newData.ranking"></fish-input>
            </fish-field>
              <fish-button @click="showModal = false">Close</fish-button>
              <fish-button type="primary" :loading="isAdding" @click="submitForm">Submit</fish-button>
          </fish-form>
        </fish-modal>
	</div>
</template>

<script>
	import {mapState, mapActions} from 'vuex'

	export default {
		props: {
			url: {
				type: String
			},
			category_id: {
				default: null,
				type: Number
			}
		},
		computed: {
            ...mapState ([
                'categories'
            ]),
            tableColumns() {
                return [
                    {
                        title: "Name",
                        key: 'title'
                    },
                    {
                        title: "Description",
                        key: "description"
                    },
                    {
                        title: "Ranking",
                        key: "ranking"
                    },
                    {
                        title: "Category",
                        key: "category"
                    },
                    {
                        title: "Action",
                        key: "id",
                        render: (h, record, column) => h('a', {
                            class: 'fish button primary',
                            on: {
                               click : () => {
                                    this.showEditDialog(record)
                               }
                            }
                            }, 'Edit')
                    }
                ]
            }
        },
		data () {
			return {
				thingsList: [],
				isAdding: false,
                isEditing: false,
                showModal: false,
                newData: {}
			}
		},
		methods: {
			...mapActions (['fetchCategories']),
			fetchItems () {
				this.http.get(this.url).then(resp => {
					this.thingsList = resp
				})
			},
			showModalFunction () {
                if (this.categories.length == 0) {
                    this.fetchCategories()
                }
                this.newData = {}
                this.isEditing = false
                this.showModal = true
            },
            submitForm () {
                let payload = this.newData
                if (this.isEditing) {
                    this.http.put(`/things/${payload.id}/`, payload).then(resp => {
                        this.fetchItems()
                        this.$message.success('Edited successfully', 5000)
                        this.showModal = false
                    })
                } else {
                    this.http.post('/things/', payload).then(resp => {
                        this.thingsList.push(resp);
                        this.showModal = false;
                        this.newData = {}
                        this.$message.success('You have successfully added an item', 5000)
                    })
                }
            },
            showEditDialog (record) {
                if (this.categories.length == 0) {
                    this.fetchCategories()
                }
                this.isEditing = true
                this.showModal = true
                this.newData = record
            }
		},
		mounted () {
			this.fetchItems()
		}
	}
</script>