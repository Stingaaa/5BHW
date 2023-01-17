import axios from "axios";

export async function patch(c){
    const response = await axios.patch(`http://localhost:5000/item/${c.id}`,
    {
        params:
        {
            description: c.description
        }
    });
return response.data;
}