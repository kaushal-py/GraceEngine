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
          <a class="panel-block is-active">
            <span class="panel-icon">
              <i class="fas fa-book" aria-hidden="true"></i>
            </span>
            count
          </a>
          <a class="panel-block">
            <span class="panel-icon">
              <i class="fas fa-book" aria-hidden="true"></i>
            </span>
            temperature
          </a>
          <a class="panel-block">
            <span class="panel-icon">
              <i class="fas fa-book" aria-hidden="true"></i>
            </span>
            apple
          </a>
          <a class="panel-block">
            <span class="panel-icon">
              <i class="fas fa-book" aria-hidden="true"></i>
            </span>
            {{ nls }}
          </a>
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
            :program="demojson.program">
          </ProgramView>
          </div>
        </nav>
      </div>
    </div>
    </div>
   

</div></template>

<script>
import ProgramView from '@/components/ProgramView.vue';
import json from '../assets/demo.json'
import axios from 'axios';

export default {
  
  name: 'demo',
  components:{
    ProgramView,
  },

  data: function(){

    return{
      demojson: {},
      nls: "",
    }
  },

  methods:{
    getProgram: function(){
      axios.get('http://localhost:5000/', {
        params:{
          nls: this.nls
        }
      }).then(
        response => (this.demojson = response.data)
      )
    }
  }
};
</script>

<style lang="scss" scoped>
  // #program-block{
  //   min-height: 300px;
  // }
</style>
