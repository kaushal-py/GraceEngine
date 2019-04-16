<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- HelloWorld msg="Welcome to Your Vue.js App"/> -->

<div class="container">
  <button @click="createNewSession" class="button is-large is-primary">Start a new Session</button> &nbsp;
  <router-link :to="{ name: 'demo', params: { sessionid: sessionId }}" class="button is-large is-primary">Join Session</router-link> &nbsp;
  <input type="text" v-model="sessionId" placeholder="Enter Session ID">
</div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import axios from "axios";

export default {
  name: 'home',
  components: {
    HelloWorld,
  },
  data: function (){
    return {
      sessionId: null,
      abc: 0,
    }
  },
  methods: {
    createNewSession: function(){
      this.getNewSessionId();
    },
    getNewSessionId: function() {
      axios
        .get("http://localhost:5000/getsessionid", {})
        .then(response => {
          this.sessionId = response.data.sessionid;
          this.$router.push({
            // name: 'demo',
            // params: {
            //   sessionId: this.sessionId,
            // }
            path: `/demo/${this.sessionId}`
          });
        });

    },
  }
};
</script>
