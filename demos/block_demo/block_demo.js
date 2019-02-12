var app = new Vue({
    el: '#app',
    data: {
      temp_input: '',
      blocks: [],
    },
    methods: {
      // addBlock: function(block){
      //   this.blocks.push({name:"print", message:"hello"})
      // },
      processInput: function(){
        var inp = this.temp_input.toLowerCase();
        var inp_list = inp.split(" ");
        

        if (inp_list[0] == "print"){
          var block = {
            name:"print",
            value: inp_list.slice(1, inp_list.length).join(" ")
          };

          console.log(block.name, block.value);

          this.blocks.push(block);
        }
      },
    }
});

