<script setup>
import { search } from './api.js';
import { patch } from './edit.js';
</script>

<template>
  <div>
    <input v-on:keyup.enter="onEnter" v-model="keyword" placeholder="Suchbegriff eingeben!"/>
    <table>
      <tr v-for="r in res">
          <td class="img-container">
            <img :src="'http://webapp.uibk.ac.at/ubi/cat/'+r['thumb']">
          </td>
          <td class="discription-container">
            <textarea  v-model="r['description']" :ref="r['id']" cols="40" rows="20"></textarea>
          </td>
          <td class="button-container">
            <button @click="edit(r)">Edit Text</button>
          </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      keyword: "hallo",
      res : "",
      desc:""
    }
  },
  methods:{
    onEnter: async function(){
      this.res = await search(this.keyword)
    },
    async edit(entry){
      await patch(entry)
    }
  }
}
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
