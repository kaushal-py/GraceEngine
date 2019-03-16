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
   </div>

   <div class="program">
     <Card 
      :card-number="cardNumber"
      :card-type="cardType"
      :display="display"></Card>
   </div>
  </div>
</template>

<script>
import Card from '@/components/Card.vue';

export default {
  name: 'about',
  components:{
    Card,
  },

  data: function(){

    return{
      cardId:"variable_setter",
      cardNumber:1,
      cardType:[true,true, false, false, false, true, 0],
      cardColor:"color_normal",
      display:[
          {
              val_type:"text",
              text:"set"
          },
          {
              val_type:"sticker",
              sticker_name:"variable",
              sticker_value:"count"
          },
          {
              val_type:"text",
              text:"to"
          }
      ]
    }
  },
};
</script>

