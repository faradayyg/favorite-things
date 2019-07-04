<template>
  <fish-row>
    <fish-col span="8" push="8" class="">
      <fish-card fluid class="login-form">
        <fish-form ref="form">
          <h2>Login Below</h2>
          <fish-field :rules="[{ required: true, message: 'The username field is required'}]">
            <fish-input :iconLeft="true" v-model="username" hint="Please enter your email" icon="fa fa-user"></fish-input>
          </fish-field>
          <fish-field :rules="[{ required: true, message: 'The password field is required'}]">
            <fish-input :iconLeft="true" v-model="password" type="password" hint="Please enter your password" icon="fa fa-lock"></fish-input>
          </fish-field>
          <fish-button :loading="isLoading" @click="submitLoginForm" type="primary">Submit</fish-button>
        </fish-form>
      </fish-card>
    </fish-col>
  </fish-row>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    data () {
      return {
        username: null,
        password: null,
        isLoading: false,
      }
    },
    methods: {
      ...mapActions([
        'login'
      ]),
      submitLoginForm () {
        this.isLoading = true
        this.http.post('/login/', {username: this.username, password: this.password}).then(resp => {
          this.login(resp)
          window.location.reload()
        }).catch(error => {
          if (error && error.detail) {
            this.$message.error(error.detail, 5000)
          } else {
            console.log(error)
            this.$message.error("An error occurred, please try again", 5000)
          }
        }).then(finish => {
          this.isLoading = false
        })
      }
    }
  }
</script>

<style>
  .login-form {
    margin-top: 40px;
  }
</style>
