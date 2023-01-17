import axios from "axios";

export async function search(q){
    const response = await axios.get(`http://localhost:5000/search/${q}`, {});
    console.log(response.data)
    return response.data;
}