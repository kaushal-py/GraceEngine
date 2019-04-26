<template>
    <section class="hero is-info is-fullheight" id="parent-section">
        <div class="hero-head">
            <nav class="navbar">
                <div class="container">
                    <div class="navbar-brand">
                        <a class="navbar-item" href="../">
                            GraceEngine
                        </a>
                        <span class="navbar-burger burger" data-target="navbarMenu">
                            <span></span>
                            <span></span>
                            <span></span>
                        </span>
                    </div>
                    <div id="navbarMenu" class="navbar-menu">
                        <div class="navbar-end">
                            <span class="navbar-item">
                                <a class="button is-white is-outlined" href="#">
                                    <span class="icon">
                                        <i class="fa fa-home"></i>
                                    </span>
                                    <span>Home</span>
                                </a>
                            </span>
                            
                            <span class="navbar-item">
                                <a class="button is-white is-outlined" href="https://github.com/kb-studios/GraceEngine">
                                    <span class="icon">
                                        <i class="fa fa-github"></i>
                                    </span>
                                    <span>View Source</span>
                                </a>
                            </span>
                        </div>
                    </div>
                </div>
            </nav>
            </div>

            <div class="hero-body">
                <div class="container has-text-centered">
                    <div class="column is-6 is-offset-3">
                        <div class="level-item has-text-centered">
                            <button class="button is-link is-inverted is-large" @click="createNewSession" >Start a new Session</button>
                        </div><br><br>
                        <h1 class="title">
                            An online Programming Engine
                        </h1>
                        <h2 class="subtitle">
                            Grace Engine is an online tool to convert spoken natural language sentences to Python code segments.
                        </h2>
                        <div class="level" id="button-group">
                            <!-- <div class="level-item has-text-centered">
                                <button class="button is-link is-inverted is-large" @click="createNewSession" >Start a new Session</button>
                            </div> -->
                            <div class="level-item has-text-centered">
                                <!-- <a class="button is-link is-inverted is-large">Inverted</a> -->
                                <!-- <router-link :to="{ name: 'demo', params: { sessionid: sessionId }}" class="button is-link is-inverted is-large">Join Session</router-link> -->
                                <!-- <input type="text" v-model="sessionId" placeholder="Enter Session ID"> -->
                                <div class="field has-addons">
                                <div class="control">
                                    <input class="input is-large" type="text" v-model="sessionId" placeholder="Enter session ID">
                                </div>
                                <div class="control">
                                    <!-- <a class="button is-info is-inverted is-large" router-link :to="{ name: 'demo', params: { sessionid: sessionId }}"> -->
                                    <router-link :to="{ name: 'demo', params: { sessionid: sessionId }}" class="button is-link is-inverted is-large">Join Session</router-link>
                                    <!-- </a> -->
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

</section>
</template>

<style>
#parent-section
{

}
</style>


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
