<template>
    <div>
        <fish-modal :title="((editing == null) ? 'Add new ' : 'Edit ') + 'category'" :visible.sync="showModal">
              <fish-form>
                  <fish-field label="Category Name">
                    <fish-input v-model="categoryName"></fish-input>
                      <fish-button @click="showModal = false">Close</fish-button>
                      <fish-button type="primary" @click="saveCategory" :loading="isWorking" >Save</fish-button>
                  </fish-field>
              </fish-form>
        </fish-modal>
        <fish-button type="positive" @click="showAddModal">Add Category</fish-button>
        <fish-table :columns="columns" :data="categories"></fish-table>
    </div>
</template>

<script>
    import {mapActions, mapState} from 'vuex'
    export default {
        computed: {
            ...mapState(['categories']),
            columns () {
                return [
                    {
                        title: "Category Name",
                        key: "name"
                    },
                    {
                        title: "Created time",
                        key: "created_at",
                        render: (h, record, column) => h('div', (new Date(record.created_at)).toDateString())
                    },
                    {
                        title: "Actions",
                        key: "id",
                        render: (h, record, column) => h('div',
                            [
                                h('a', {
                                    class: 'fish',
                                    on: {
                                        click: () => {
                                            this.viewCategoryItems(record)
                                        }
                                    }
                                }, 'View Items'),
                                h('a', {
                                    class: 'fish button primary',
                                    style: 'margin-left: 10px',
                                    on: {
                                        click: () => {
                                            this.editCategory(record)
                                        }
                                    }
                                },'Edit'),
                                h('a', {
                                    class: 'fish button negative',
                                    style: 'margin-left: 10px',
                                    on: {
                                        click: () => {
                                            this.deleteCategory(record)
                                        }
                                    }
                                },'Delete')
                            ]
                        )
                    }
                ]
            }
        },
        data () {
            return {
                editing: false,
                categoryName: '',
                showModal: false,
                isWorking: false
            }
        },
        methods: {
            ...mapActions(['fetchCategories']),
            deleteCategory (record) {
                this.confirmDialog('Sure to delete?').then(resp => {
                    this.http.delete(`/things/categories/${record.id}/`).then(resp => {
                        this.fetchCategories()
                    })
                })
            },
            editCategory (record) {
                this.editing = record;
                this.showModal = true;
                this.categoryName = record.name
            },
            saveCategory () {
                this.isWorking = true
                if (this.editing == null) {
                    this.http.post('/things/categories/', {name: this.categoryName}).then(resp => {
                        this.fetchCategories();
                        this.$message.success('You have added a new category');
                        this.categoryName = null;
                        this.showModal = false;
                    }).then(() => {
                        this.isWorking = false
                    }).catch(err => {
                        this.$message.error('An error Ocurred', 500)
                    })
                } else {
                    this.http.put(`/things/categories/${this.editing.id}/`, {name: this.categoryName}).then(resp => {
                        this.fetchCategories();
                        this.$message.success('Category edited successfully');
                        this.categoryName = null;
                        this.showModal = false;
                    }).then(() => {
                        this.isWorking = false
                    }).catch(err => {
                        this.$message.error('An error Ocurred', 500)
                    })
                }
            },
            showAddModal () {
                this.showModal = true
                this.editing = null
                this.categoryName = ''
            },
            viewCategoryItems (record) {
                this.$router.push({
                    name: 'things.category.items',
                    params: {id: record.id}
                })
            }
        },
        mounted () {
            this.fetchCategories()
        }
    }
</script>
