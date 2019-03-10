<template>
  <div class="home">
    <section class="hero is-primary">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">
        Hero title
      </h1>
      <h2 class="subtitle">
        Hero subtitle
      </h2>
    </div>
  </div>
</section>
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
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
