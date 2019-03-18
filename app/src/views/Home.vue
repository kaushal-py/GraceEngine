<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- HelloWorld msg="Welcome to Your Vue.js App"/> -->

<div class="container">
  <router-link to="/demo" class="button is-large is-primary">Create Session</router-link> &nbsp;
  <router-link to="/" class="button is-large is-primary">Join Session</router-link> &nbsp;
</div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: 'home',
  components: {
    HelloWorld,
  },
};
</script>
