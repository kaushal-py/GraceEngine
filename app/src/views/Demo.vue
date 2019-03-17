<template>
  <div class="about">
   <div class="container">
     <div class="columns is-centered">
     <div id="user-sentence" class="column is-four-fifths field has-addons">
      <div class="control is-expanded">
        <input class="input" type="text" placeholder="Enter your natural language sentence here">
      </div>
      <div class="control">
        <a class="button is-info">
          Search
        </a>
      </div>
    </div>
   </div>

   <div class="has-text-left">
      <ProgramView
        :program="demojson.program">
      </ProgramView>
    </div>
  </div>

   </div>
    
</template>

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

