<template>
  <div id="app">
    <!-- <div id ="topnav">
       <h1 class="title is-1">
        <span class="has-text-info has-text-weight-light">
          Grace</span>
        <span><strong class="has-text-link has-text-weight-bold">Engine</strong></span>
      </h1>
        <img id="banner" src="./assets/GraceEngine.png">
    </div> -->

    <!-- <div class="gradient">
    </div> -->
    <router-view/>

    <!-- <div>Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div> -->

  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Montserrat');
@import "~bulma/sass/utilities/_all";
@import url("https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons");

$color-background: #fae596;
$color-text1: #3fb0ac;
$color-text2: #173e43;
$color-sec: #dddfd4;
$primary: #8b5bdf;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.box{
  font-family: 'Montserrat', sans-serif;
}

#topnav{
  margin-bottom: 120px;
}

// #banner{
//   display: block;
//   object-fit: cover;
//   height: 470px;
//   width: 100%;
// }

.gradient{
  background-image: linear-gradient(#173761, white);
  height: 500px;
}
</style>
