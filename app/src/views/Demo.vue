<template><div>
   <div class="container">
     <div class="columns is-centered">
     <div id="user-sentence" class="column is-four-fifths field has-addons">
      <div class="control is-expanded">
        <input v-model="nls" class="input is-primary is-rounded" type="text" placeholder="Enter your natural language sentence here">
      </div>
      <div class="control">
        <a class="button is-primary is-rounded" @click="getProgram">
          Speak
        </a>
      </div>
    </div>
   </div>
   </div>

    <div>
      <SpeechText :text.sync="nls" @speechend="speechEnd"></SpeechText>
    </div>

    <br>

    <div class="container is-fluid">
    <div class="columns">
      <div class="column is-one-fifth">
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
      </div>
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
    }
  }
};
</script>

<style lang="scss" scoped>
  #program-block{
    // min-height: 300px;
    overflow-x: scroll;
  }
</style>
