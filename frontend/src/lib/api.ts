import { PUBLIC_API_URL } from "$env/static/public"
import type { Cookies } from "@sveltejs/kit"
import { jwtDecode } from "jwt-decode"


export async function apiFetch(url: string, options: RequestInit, accessToken?: string){
    let apiUrl = PUBLIC_API_URL + url
    const requestHeaders = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': accessToken ? 'Bearer ' + accessToken : ""
    }
    options.headers = {
        ...requestHeaders,
        ...options.headers,

    }

    return fetch(apiUrl, options)
}

export class Response {
    success: boolean 
    data!: object | any
    
    constructor(success?: boolean, data?: object) {
        this.success = success || false
        this.data = data || {}
    }

    setResponse(success: boolean, data: object) {
        this.success = success
        this.data = data
    }

    getResponse() {
        return {
            success: this.success,
            data: this.data
        }
    }

}









