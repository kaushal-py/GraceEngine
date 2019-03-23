<template><div class="outer-div">

  <div class="tile">
    <div class="tile is-vertical is-9">
      <div id="topbar" class="tile">
        <div id="logo-div" class="tile is-2">
            <br>
            <h1 class="subtitle is-3">GraceEngine</h1>
        </div>
        
        <div class="tile is-vertical">      
          
          <div class="tile">
            <SpeechText :text.sync="nls" @speechend="speechEnd"></SpeechText>
          </div>      

          <div class="tile is-parent">
            <div class="tile is-child column is-paddingless is-marginless">
              <div class="speech-text">
                <div class="field has-addons">
                  <p class="control">
                    <a class="button is-static is-rounded is-medium">
                      Grace$>
                    </a>
                  </p>
                  <p class="control is-expanded">
                    <input class="input is-rounded is-medium" type="text" placeholder="Your sentence will appear here.">
                  </p>
                
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="tile">
        hello world
      </div>

    </div>
    <div class="tile is-3"> 
      Grace    
    </div>
  </div>

      <!-- <div class="tile">
        <div class="tile is-vertical">
          hello world
        </div>
      </div> -->
    <br> <br>

    <div class="container is-fluid">
    <div class="columns">
      <!-- <div class="column is-one-fifth">
        <nav class="panel">
          <p class="panel-heading">
            Variables
          </p>
          <div class="panel-block">
            <p class="control has-icons-left">
              <input class="input is-small" type="text" placeholder="search">
              <span class="icon is-small is-left">
                <i class="fas fa-search" aria-hidden="true"></i>
              </span>
            </p>
          </div>
          <div v-for="variable in variables" :key="variable">
            <a class="panel-block">
              <span class="panel-icon">
                <i class="fas fa-book" aria-hidden="true"></i>
              </span>
              {{variable}}
            </a>
          </div>
          
          <div class="panel-block">
            <button class="button is-link is-outlined is-fullwidth">
              Create new Variable
            </button>
          </div>
        </nav>
      </div> -->
      <div class="column">
        <nav class="panel has-text-left">
          <p class="panel-heading">Program</p>
          <div id="program-block" class="panel-block">
          <ProgramView
            :program="cardjson.program">
          </ProgramView>
          </div>
        </nav>

        <nav class="panel has-text-left">
          <p class="panel-heading">Code</p>
          <div id="program-block" class="panel-block"
            v-html="code">
          </div>
        </nav>
      </div>


    </div>
    </div>
   

</div></template>

<script>
import ProgramView from '@/components/ProgramView.vue';
import SpeechText from '@/components/SpeechText.vue';
import json from '../assets/demo.json'
import axios from 'axios';

export default {
  
  name: 'demo',
  components:{
    ProgramView,
    SpeechText,
  },

  // mounted:function(){
  //   this.getProgram();
  //   this.getCode();
  // },

  data: function(){

    return{
      cardjson: {},
      nls: "",
      code: "",
      variables: [],
      sentences: null,
    }
  },

  watch: {
    nls: function(){
      if( this.nls[this.nls.length -1] == ' '){
        this.getProgram();
      }
    },
    code: function(){
      this.nls = "";
    }
  },

  methods:{
    getProgram: function(){
      axios.get('http://localhost:5000/put', {
        params:{
          nls: this.nls
        }
      }).then(
        response => (this.cardjson = response.data)
      );
      this.getCode();
      this.getVariables();
      console.log("Get code called");
    },
    getCode: function(){
      axios.get('http://localhost:5000/code', {
      }).then(
        response => (this.code = response.data.code)
      )
    },
    getVariables: function(){
      axios.get('http://localhost:5000/variables', {
      }).then(
        respose => (this.variables = respose.data.variables)
      )
    },
    speechEnd ({sentences, text}) {
      console.log('text', text)
      console.log('sentences', sentences)
      this.sentences = sentences
    },
    clearPad: function(){
      this.nls = ""
    }
  }
};
</script>

<style lang="scss" scoped>
@import "~bulma/sass/utilities/_all";
$panel-heading-background-color: $primary;
$panel-heading-color: white;
#program-block{
  // min-height: 300px;
  overflow-x: auto;
}

#logo-div{
  text-align: center;
  background-color: $light;
}

#topbar{
  border-bottom: 1px solid gray;
}

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
