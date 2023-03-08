<template>
  <header>
    

  </header>

  <main class="container mt-4 overflow-hidden">
    <div class="flex text-lg p-2 border min-w-min max-w-fit">
      <Dropdown type="countries" @onInputChange="inputChangeCountry($event)"/>
      <Dropdown type="events" @onInputChange="inputChangeEvent($event)"/>
    </div>
    <div class="flex flex-none gap-3 sm:flex-col xl:flex-row">
      <DataTable v-if="currCountry != undefined" 
        className="p-4 mt-4 mb-4 border sm:w-2/5 lg:w-full max-w-[50%]" 
        :data="medalsComb"
        :columns="['Medaille', 'Anz']"
      />
      <PlotComp v-if="medalsGender.length != 0" type="bar" :xValue="['Gold', 'Silber', 'Bronze']" :yValues="medalsGender" title="Male vs Female Medal"/>
    </div>
    <div class="height-part">
      <PlotComp v-if="renderAll == true" type="scatter" :xValue="years" :yValues="heights" type_="height" title="Age-Height-AVG"/>
    </div>
    <div class="height-part">
      <PlotComp v-if="renderAll == true" type="bar" :xValue="['Gold', 'Silber', 'Bronze']" :yValues="medalsEvent" title="Medal per Event"/>
    </div>
    <div class="height-part">
      <PlotComp v-if="renderAll == true" type="pie" :xValue="weight_avg.xValues" :yValues="weight_avg.yValues" title="Top 5 Weight Avg" type_="height"/>
    </div>
  </main>
</template>

<script>
import Dropdown from './components/UI/Dropdown.vue';
import DataTable from './components/data.vue';
import PlotComp from './components/comp.vue';
import axios from 'axios';
export default {
  components: {
    Dropdown, 
    DataTable,
    PlotComp
  },
  data() {
    return {
      currCountry: undefined,
      currEvent: undefined,
      medalsComb: [],
      medalsGender: [],
      renderAll: false,
      years: [],
      heights: [],
      medalsEvent: [],
      weight_avg: {
        xValues: [],
        yValues: []
      }
    }
  },
  async mounted() {
    
  },
  methods: {
    async inputChangeEvent(e){
      this.currEvent = e
      this.renderAll = false
      await this.getHeight()
      await this.getMedalsEvent()
      this.renderAll = true
    },
    async inputChangeCountry(e){
      this.currCountry = e
      await this.getMedalsPerSex()
      await this.getHeight()
      await this.getWeight()
      this.renderAll = false
      let res_medals = await axios.get(this.$hostname + `medals/${e}`)
      
      this.medalsComb = res_medals.data
      this.renderAll = true
    },
    async getMedalsPerSex(){
      let res_gender_medals = await axios.get(this.$hostname + 'count_by_sex')
      
    res_gender_medals.data.forEach(element => {
        element[0] = element[0]=='M'? 'Male': 'Female'
      })
      res_gender_medals = res_gender_medals.data
      
      let multibleFemales = res_gender_medals.filter(element => element.includes('Female'))
      let multibleMale = res_gender_medals.filter(element => element.includes('Male'))
      

    let female = [
      "Female",
      multibleFemales.find(element => element.includes('Gold'))[2],
      multibleFemales.find(element => element.includes('Silver'))[2],
      multibleFemales.find(element => element.includes('Bronze'))[2],
    ]
    let male = [
      "Male",
      multibleMale.find(element => element.includes('Gold'))[2],
      multibleMale.find(element => element.includes('Silver'))[2],
      multibleMale.find(element => element.includes('Bronze'))[2],
    ]
    this.medalsGender = [male, female]
    },
    async getWeight(){
      let res = await axios.get(`${this.$hostname}weight/${this.currCountry}`)
      let res1 = res.data
      res1 = res1.sort((a, b) => {
        return Object.values(a)[0] - Object.values(b)[0]
      })
      res1 = res1.slice(-5)
      let xValues = []
      let yValues = []
      res1.forEach(e => {
        xValues.push(Object.keys(e)[0])
        yValues.push(Object.values(e)[0])
      })
      this.weight_avg = {
        xValues: yValues,
        yValues: xValues
      }
    },
    async getHeight(){
      let res = await axios.get(`${this.$hostname}height/${this.currCountry}`)
      res = this.$sortByKey(res.data, 'age')
      let handler = {
        get: function(target, name){
          return target.hasOwnProperty(name) ? target[name] : 0
        }
      }
      let age_obj = {}
      let height_obj = {}
      let age_count = new Proxy(age_obj, handler)
      let height_avg = new Proxy(height_obj, handler)
      res.forEach(i => {
        age_count[i.age] += 1
        height_avg[i.age] += i.height
      })
      Object.keys(age_obj).forEach(key => {
        height_obj[key] /= age_obj[key]
        this.years.push(key)
        this.heights.push(height_obj[key])
      })
      this.years = Object.values(this.years)
      this.heights = Object.values(this.heights)
    },
    async getMedalsEvent(){
      let res = await axios.get(`${this.$hostname}event/${this.currEvent}`)
      this.medalsEvent = res.data
    },
  }
}
</script>

<style scoped>
[v-cloak]{
  display: none;
}
</style>
<!--Habe Tailwind eingebaut weil bootstrap nicht so wollte wie ich wollte :)-->
<style src="./assets/tailwind.css"></style>
<style src="./assets/bootstrap.css"></style>