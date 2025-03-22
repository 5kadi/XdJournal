import axios from "axios"
import { API_URL } from "$env/static/private"

export const api = axios.create(
    {
        baseURL: API_URL
    }
) //new instance with custom config







