<script setup>
// import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <!-- <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main> -->
  <title>Minesweeper</title>
  <div @mousedown="field" @click="minefield" id="field" class="field">
  </div>
</template>

<script>
export default {
  mounted() {
    this.minefield(document.getElementById("field"))
  },
  methods:{
    field(event) {
      const x = event.clientX - event.currentTarget.offsetLeft;
      const y = event.clientY - event.currentTarget.offsetTop;
      this.minefield(event.currentTarget)
    },
    minefield(elem){
      const width = elem.offsetWidth;
      const height = elem.offsetHeight;
      var field = new Array(9)
      for(var i = 0; i < 9; i++){
        field[i] = new Array(9)
      }
      const minefield = document.getElementById("field")
      for(var i = 0; i < 9; i++){
        for(var j = 0; j < 9; j++){
          field[i][j] = 0
          const img = document.createElement("img")
          img.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Minesweeper_0.svg/800px-Minesweeper_0.svg.png"
          img.margin = 0
          img.padding = 0
          img.width = width/9
          img.height = height/9
          const div = document.createElement("div")
          div.id = i+""+j
          div.style.display = "flex"
          div.style.position = "absolute"
          div.style.marginLeft = img.width*i + "px"
          div.style.marginTop = img.height*j + "px"
          div.style.padding = 0
          div.appendChild(img)
          minefield.appendChild(div)
        }
      }
      document.cookie = "field="+field
    }
  }
};
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

body, #app {
  height: 100vh;
  margin: 0;
}

.test{
  width: 100px;
  height: 100px;
  background-color: brown;
}

.field {
  padding: 0px;
  margin: 0px;
  width: 70vw;
  height: 70vh;
}

img{
  display: flex;
  padding: 0px;
  margin: 0px;
}
</style>