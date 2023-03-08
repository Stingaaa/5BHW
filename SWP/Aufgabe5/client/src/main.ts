import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

function sortByKey(arr, key) {
    return arr.sort(function(i, j) {
        var a = i[key]; var b = j[key];
        return ((a < b) ? -1 : ((a > b) ? 1 : 0));
    });
}

app.config.globalProperties.$sortByKey = sortByKey;

app.config.globalProperties.$hostname = 'http://127.0.0.1:5000/'

app.mount('#app')
