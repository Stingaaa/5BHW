<template>
  <VuePlotly className="sm:max-w-full lg:max-w-[50%]" :data="data" :layout="layout" :display-mode-bar="false"/>
</template>

<script>
import { VuePlotly } from 'vue3-plotly'
export default{
  components: {
      VuePlotly
  },
  props: ['xValue', 'yValues', 'type', 'type_', 'title'],
  data() {
      return{
          data: [],
          layout: {
              title: ''
          }
      }
  },
  beforeMount(){
      let data = []
      if(this.type_ != 'height'){
          let x = 0
          this.yValues.forEach(yValue=> {
              let trace_name = yValue[0]
              yValue = yValue.slice(1)
              data.push({
                  x: this.xValue,
                  y: yValue,
                  type: this.type,
                  name: trace_name
              })
          })
          
      }else if(this.type == 'pie'){
          data.push({
              values: this.xValue,
              labels: this.yValues,
              type: this.type
          })
      }else{
          data.push({
              x: this.xValue,
              y: this.yValues,
              type: this.type,
          })
      }
      this.layout.title = this.title
      this.data = data
  },
}
</script>