<template>
  <div class="outer-div">
    <div class="tile">
      <div class="tile is-vertical is-9">
        <div id="topbar" class="tile">
          <div id="logo-div" class="tile is-2">
            <img id="logo-img" src="../assets/Logo.png" alt="Logo Grace">
          </div>

          <div id="search-bar" class="tile is-vertical">
            <br>
            <div class="tile">
              <SpeechText :text.sync="nls" @speechend="speechEnd"></SpeechText>
            </div>

            <div class="tile is-parent">
              <div class="tile is-child column is-paddingless is-marginless">
                <div class="speech-text">
                  <div class="field has-addons">
                    <p class="control">
                      <a class="button is-static is-rounded is-medium">Grace$></a>
                    </p>
                    <p class="control is-expanded">
                      <input
                        v-model="nls"
                        class="input is-rounded is-medium"
                        type="text"
                        placeholder="Your sentence will appear here."
                      >
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="tile">
          <div id="left-background" class="tile is-2 has-background-light is-hidden-mobile"></div>

          <div class="tile">
            <div class="container is-fluid is-marginless">
              <div class="tile">
                Results updated in {{time}} seconds.     
              </div>
              <nav class="panel has-text-left">
                <div class="panel-heading">
                  <div class="tile">
                    <div class="tile">
                      Program        
                    </div>
                    <div class="tile">
                      <div class="buttons is-right">
                        <button @click="clearProgram" class="button is-danger">
                          Clear &nbsp;<i class="fas fa-times"></i>
                        </button>
                      </div>
                    </div>
                  </div> 
                </div>
                <div class="panel-block program-block">
                  <ProgramView 
                    :program="cardjson.program"
                    :inserted="cardjson.inserted_card_number"
                    :current="cardjson.current_card_number">
                  </ProgramView>
                </div>
              </nav>

              <nav class="panel has-text-left">
                <div class="panel-heading">
                  <div class="tile">
                    <div class="tile">
                      Code and Output               
                    </div>
                    <div class="tile">
                      <div class="buttons is-right">
                        <button @click="getOutput" class="button is-warning">
                          Play &nbsp;<i class="fas fa-play"></i>
                        </button>
                      </div>
                    </div>
                  </div> 
                </div>
                <div class="panel-block program-block">
                  <div class="tile">
                    <div class="tile">
                      <pre>
{{ code }}
                      </pre>
                    </div>
                    <div class="tile">
                      <pre>
{{ output }}
                      </pre>
                    </div>
                  </div>
                 
                </div>
              </nav>
            </div>
          </div>
        </div>
      </div>

      <div class="tile is-3">
        <div class="container">
            <br><br>
          <div class="box grace-box">
              <!-- Output the suggestions -->
              <div v-if="suggestions != null && suggestions.length>0" class="has-text-weight-semibold">
                  Suggestions
                  <hr>
              </div>
              <div v-for="suggestion in suggestions">
                  <p>{{ suggestion }}</p>
              </div>

                <div v-if="suggestions.length==0">
                    Hello There!<br> I am Grace Hopper and I am here to help you.
                    I will be helping you with suggestions and any other issues you have.
                    Start by saying "print".
                </div>
            <img id="grace-hopper" src="../assets/hopper.png" alt="Grace Hopper">
          </div>
        </div>
      </div>
    </div>

    <!-- <div class="tile">
        <div class="tile is-vertical">
          hello world
        </div>
    </div>-->
    <br>
    <br>
  </div>
</template>

<script>
import ProgramView from "@/components/ProgramView.vue";
import SpeechText from "@/components/SpeechText.vue";
import json from "../assets/demo.json";
import axios from "axios";

export default {
  name: "demo",
  components: {
    ProgramView,
    SpeechText
  },

  mounted:function(){
    console.log("create function called");
    console.log("SESSION ID: " + this.$route.params.sessionid);
    this.sessionId = this.$route.params.sessionid;

    this.getCards();
    this.getCode();

    setInterval(() => {
      this.getCards();
      this.getCode();
    }, 2000);

  },

  created: function(){
    let recaptchaScript = document.createElement('script');
    recaptchaScript.setAttribute('src', 'https://use.fontawesome.com/releases/v5.3.1/js/all.js');
    document.head.appendChild(recaptchaScript);
  },

  data: function() {
    return {
      cardjson: {},
      nls: "",
      code: "",
      variables: [],
      sentences: null,
      output: "",
      updated: false,
      suggestions: [],
      sessionId: 0,
      time: 0.0,
    };
  },

  watch: {
    nls: function() {
      if (this.nls != null && this.nls[this.nls.length - 1] == " ") {
        this.insertCard();
      }
    },
    code: function() {
      this.nls = "";
    },
    updated: function(){
      this.nls = "";
      this.getCards();
      this.updated = false;
    }
  },

  methods: {

    insertCard: function() {
      axios
        .get("http://localhost:5000/put", {
          params: {
            nls: this.nls,
            sessionid: this.sessionId,
          }
        })
        .then(response => {
          this.cardjson = response.data;
          this.time = this.cardjson.time;
      });
      
      this.getCode();
      this.getVariables();
      this.getUpdates();
      this.getSuggestions();
      console.log("Get code called");
    },
    getCards: function() {
      axios
        .get("http://localhost:5000/get", {
          params: {
            sessionid: this.sessionId
          }
        })
        .then(response => (this.cardjson = response.data));
    },
    getCode: function() {
      axios
        .get("http://localhost:5000/code", {
          params: {
            sessionid: this.sessionId
          }
        })
        .then(response => (this.code = response.data.code));
    },
    getOutput: function() {
      axios
        .get("http://localhost:5000/output", {
          params: {
            sessionid: this.sessionId
          }
        })
        .then(response => (this.output = response.data.output));
    },
    getVariables: function() {
      axios
        .get("http://localhost:5000/variables", {
          params: {
            sessionid: this.sessionId
          }
        })
        .then(respose => (this.variables = respose.data.variables));
    },
    getUpdates: function() {
      axios
        .get("http://localhost:5000/updates", {
          params: {
            sessionid: this.sessionId
          }
        })
        .then(respose => (this.updated = respose.data.updated));
    },
    clearProgram: function() {
      axios
        .get("http://localhost:5000/clear", {
          params: {
            sessionid: this.sessionId
          }
        });
      this.getCards();
      this.getCode();
      this.getOutput();
    },
    getSuggestions: function() {
        axios
        .get("http://localhost:5000/suggest", {
            params: {
              nlstatement: this.nls,
              sessionid: this.sessionId,
          }
        })
        .then(respose => (this.suggestions = respose.data.suggestions));
    },
    speechEnd({ sentences, text }) {
      console.log("text", text);
      console.log("sentences", sentences);
      this.sentences = sentences;
    },
    clearPad: function() {
      this.nls = "";
    }
  }
};
</script>

<style lang="scss" scoped>
@import "~bulma/sass/utilities/_all";
$panel-heading-background-color: $primary;
$panel-heading-color: white;
.program-block {
  // min-height: 300px;
  white-space: nowrap;
  overflow-x: auto;
}

#logo-div {
  text-align: center;
  background-color: $primary;
}

#logo-img {
  margin-top: 20px;
  margin-left: 30px;
  height: 100px;
}

#search-bar {
  border-bottom: 1px solid #eee;
}

#topbar {
  max-height: 100px;
}

#grace-hopper {
  height: 200px;
  z-index: 20;
  position: relative;
  bottom: -175px;
  left: 40%;
}

.grace-box {
  // margin-top: 250px;
}

#left-background {
  min-height: 100vh;
}

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
