<script setup>
</script>

<template>
  <title>Minesweeper</title>
  <div oncontextmenu="return false" @mouseup="updateField" @mousedown.once="laymines" @click="minefield" id="field" class="field">
  </div>
</template>

<script>
export default {
  mounted() {
    document.cookie = "Max-Age=999999"
    document.cookie = "gameover=false"
    this.initfield(document.getElementById("field"))
  },
  methods:{
    field(event) {
      const x = event.clientX - event.currentTarget.offsetLeft
      const y = event.clientY - event.currentTarget.offsetTop
    },
    initfield(elem){
      const width = elem.offsetWidth
      const height = elem.offsetHeight
      var field = new Array(9)
      for(var i = 0; i < 9; i++){
        field[i] = new Array(9)
      }
      const minefield = document.getElementById("field")
      for(var i = 0; i < 9; i++){
        for(var j = 0; j < 9; j++){
          field[i][j] = 0
          const img = document.createElement("img")
          img.id = "img"+i+""+j
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
    },
    //0 = unknown tile  https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Minesweeper_0.svg/800px-Minesweeper_0.svg.png
    //1 = number tile 
    //  0 https://lh3.googleusercontent.com/61Nza9pnCkEGDH42MiFB4khcy796SpdmcMASHFZviSkGpWm7AczBVfs7lAp5pSA5WMCJSPwuWOR_pQPjeeJP
    //  1 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/4f6b7a09.png?v=0
    //  2 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/b037cfbb.png?v=0
    //  3 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/d99a267c.png?v=0
    //  4 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/30c00eb3.png?v=0
    //  5 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/005db999.png?v=0
    //  6 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/c3cfe237.png?v=0
    //  7 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/8b13d806.png?v=0
    //  8 https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/d718331e.png?v=0
    //2 = flag tile https://banner2.cleanpng.com/20180325/kqe/kisspng-minesweeper-computer-icons-bing-maps-video-game-mines-5ab7a191c79531.0286407715219838898175.jpg
    //3 = mine tile https://img.itch.zone/aW1nLzEwOTQ1MjE3LnBuZw==/315x250%23c/2%2BoZa7.png
    laymines(event){
      const field = new Array(9)
      for(var i = 0; i < 9; i++){
        field[i] = new Array(9)
      }
      for(var i = 0; i < 9; i++){
        for(var j = 0; j < 9; j++){
          field[i][j] = 0
        }
      }
      const elem = document.getElementById("field")
      const width = elem.offsetWidth
      const height = elem.offsetHeight
      const x = event.clientX - event.currentTarget.offsetLeft
      const y = event.clientY - event.currentTarget.offsetTop
      const tileWidth = width/9
      const tileHeight = height/9
      const tileClicked = new Array(2)
      for(var i = 0; i < 9; i++){
        if(tileWidth*i <= x && x < tileWidth*(i+1)){
          tileClicked[0] = i
        }
        if(tileHeight*i <= y && y < tileHeight*(i+1)){
          tileClicked[1] = i
        }
      }
      field[tileClicked[1]][tileClicked[0]] = 1
      var newTile = this.laytile(tileClicked, [8,8])
      field[newTile[1]][newTile[0]] = 1
      for(var j = 0; j < 5; j++){
        newTile = tileClicked
        for(var i = 0; i < 7; i++){
          newTile = this.laytile(newTile, [8,8]) //size is 1 less because 0 is included
          field[newTile[1]][newTile[0]] = 1
        }
      }
      for(var i = 0; i < (9*9/3.5); i++){
        const randX = Math.floor(Math.random()*9)
        const randY = Math.floor(Math.random()*9)
        if(field[randX][randY] == 0){
          field[randX][randY] = 3
        }else{
          i--
        }
      }
      document.cookie = "setupfield="+field
      //alert(document.cookie)
      this.updateField(event, true)
    },
    laytile(maintile, size){
      const rand = Math.floor(Math.random()*4)
      var newtile = maintile
      switch(rand){
        case 0:
          return this.laytile(newtile, size)
        case 1: 
          if (newtile[0]+1 <= size[0]){
            newtile[0] = newtile[0]+1
            break
          }else{
            return this.laytile(newtile, size)
          }
        case 2: 
          if (newtile[1]+1 <= size[1]){
            newtile[1] = newtile[1]+1
            break
          }else{
            return this.laytile(newtile, size)
          }
        case 3: 
          if (newtile[0]-1 >= 0){
            newtile[0] = newtile[0]-1
          }else{
            return this.laytile(newtile, size)
          }
      }
      return newtile
    },
    updateField(event, all=false){
      const fields = document.cookie.split(";")
      var playerField = fields[fields.findIndex(v => v.includes("field"))]
      var temp = fields[fields.findIndex(v => v.includes("setupfield"))].replace("setupfield=", "").split(",")
      var field = []
      while(temp.length) field.push(temp.splice(0,9))
      if(all){
        for(var i = 0; i < 9; i++){
          for(var j = 0; j < 9; j++){
            const tileType = parseInt(field[j][i])
            switch (tileType){
              case 0:
                document.getElementById("img"+i+""+j).src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Minesweeper_0.svg/800px-Minesweeper_0.svg.png"
                break
              case 1:
                const srcs = ["https://lh3.googleusercontent.com/61Nza9pnCkEGDH42MiFB4khcy796SpdmcMASHFZviSkGpWm7AczBVfs7lAp5pSA5WMCJSPwuWOR_pQPjeeJP","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/4f6b7a09.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/b037cfbb.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/d99a267c.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/30c00eb3.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/005db999.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/c3cfe237.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/8b13d806.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/d718331e.png?v=0"]
                var cnt = 0
                for(var a = 0; a < 3; a++){
                  for(var b = 0; b < 3; b++){
                    if(i+a-1 > 8){
                    }
                    if(j+b-1 > 8){
                    }else{
                      if(field[j+b-1][i+a-1] == 3) cnt++
                    }
                  }
                }
                document.getElementById("img"+i+""+j).src=srcs[cnt]
                break
            }
          }
        }
      }else{
        const cookie = document.cookie.split(";")
        var gamestate = cookie[cookie.findIndex(v => v.includes("gameover"))].replace("gameover=", "")
        if (gamestate == " true"){
          window.location.reload()
          return
        }
        const elem = document.getElementById("field")
        const width = elem.offsetWidth
        const height = elem.offsetHeight
        const x = event.clientX - event.currentTarget.offsetLeft
        const y = event.clientY - event.currentTarget.offsetTop
        const tileWidth = width/9
        const tileHeight = height/9
        const tileClicked = new Array(2)
        for(var i = 0; i < 9; i++){
          if(tileWidth*i <= x && x < tileWidth*(i+1)){
            tileClicked[0] = i
          }
          if(tileHeight*i <= y && y < tileHeight*(i+1)){
            tileClicked[1] = i
          }
        }
        const fields = document.cookie.split(";")
        var playerField = fields[fields.findIndex(v => v.includes("field"))]
        var temp = fields[fields.findIndex(v => v.includes("setupfield"))].replace("setupfield=", "").split(",")
        var field = []
        while(temp.length) field.push(temp.splice(0,9))
        switch(event.button){
          case 0:
            if(field[tileClicked[1]][tileClicked[0]] == 3) {
              document.cookie = "gameover=true"
              document.getElementById("img"+tileClicked[0]+""+tileClicked[1]).src="https://img.itch.zone/aW1nLzEwOTQ1MjE3LnBuZw==/315x250%23c/2%2BoZa7.png"
              alert("You lose!")
              return
            }
            const srcs = ["https://lh3.googleusercontent.com/61Nza9pnCkEGDH42MiFB4khcy796SpdmcMASHFZviSkGpWm7AczBVfs7lAp5pSA5WMCJSPwuWOR_pQPjeeJP","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/4f6b7a09.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/b037cfbb.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/d99a267c.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/30c00eb3.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/005db999.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/c3cfe237.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/8b13d806.png?v=0","https://d3nsrxdg84ic1d.cloudfront.net/uploads/9a72bd43-31a9-414b-93c1-66c401c3ed9c/d718331e.png?v=0"]
              var cnt = 0
              for(var a = 0; a < 3; a++){
                for(var b = 0; b < 3; b++){
                  if(tileClicked[0]+a-1 > 8){
                  }else if(tileClicked[1]+b-1 > 8){
                  }else if(tileClicked[1]+b-1 < 0){
                  }else if(tileClicked[0]+a-1 < 0){
                  }else{
                    if(field[tileClicked[1]+b-1][tileClicked[0]+a-1] == 3) cnt++
                  }
                }
              }
              field[tileClicked[1]][tileClicked[0]] = 1
              document.getElementById("img"+tileClicked[0]+""+tileClicked[1]).src=srcs[cnt]
              document.cookie = "setupfield="+field
              var tempCnt = 0
              for(var i = 0; i < 9; i++){
                if(field[i].includes("0") == false){
                  tempCnt++
                  if(tempCnt == 9){
                    alert("You win!")
                    document.cookie="gameover=true"
                  }
                }
              }
              break
          case 2:
            if(field[tileClicked[1]][tileClicked[0]] == 0 || field[tileClicked[1]][tileClicked[0]] == 3){  
              var img = document.getElementById("img"+tileClicked[0]+""+tileClicked[1])
              if(img.src == "https://banner2.cleanpng.com/20180325/kqe/kisspng-minesweeper-computer-icons-bing-maps-video-game-mines-5ab7a191c79531.0286407715219838898175.jpg"){
                img.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Minesweeper_0.svg/800px-Minesweeper_0.svg.png"
              }else{
                img.src = "https://banner2.cleanpng.com/20180325/kqe/kisspng-minesweeper-computer-icons-bing-maps-video-game-mines-5ab7a191c79531.0286407715219838898175.jpg"
              }
            }
            break
        }
      }
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