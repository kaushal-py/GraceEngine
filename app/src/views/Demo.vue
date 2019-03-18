<template><div>
   <div class="container">
     <div class="columns is-centered">
     <div id="user-sentence" class="column is-four-fifths field has-addons">
      <div class="control is-expanded">
        <input class="input is-primary is-rounded" type="text" placeholder="Enter your natural language sentence here">
      </div>
      <div class="control">
        <a class="button is-primary is-rounded">
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
            marks
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
          <div class="panel-block">
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

export default {
  name: 'demo',
  components:{
    ProgramView,
  },

  data: function(){

    return{
      demojson: json
    }
  },
};
</script>

