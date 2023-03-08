<template>
    <DataTable class="table" :data="data">
        <thead>
            <tr>
                <th v-for="c in columns">{{ c }}</th>
            </tr>
        </thead>
    </DataTable>
</template>

<script>


import DataTable from 'datatables.net-vue3'
import DataTablesLib from 'datatables.net-bs5'
import axios from 'axios'

DataTable.use(DataTablesLib)
    export default {
        components: {
            DataTable
        },
        props: ['data', 'columns'],
        data() {
            return {
            }
        },
        
    }
</script>

