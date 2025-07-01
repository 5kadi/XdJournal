import { PUBLIC_API_URL } from "$env/static/public"
import sleep from "sleep-promise"


export async function apiFetch(url: string, options: RequestInit, accessToken?: string, defaultContentType = true){
    let apiUrl = PUBLIC_API_URL + url
    let requestHeaders = {'Authorization': accessToken ? 'Bearer ' + accessToken : ""}
    // @ts-ignore
    if (defaultContentType) requestHeaders['Content-Type'] = 'application/json; charset=UTF-8'
    
    options.headers = {
        ...requestHeaders,
        ...options.headers,
    }

    return fetch(apiUrl, options)
}

export class ServerResponse {
    success: boolean 
    value!: object | any
    
    constructor(success?: boolean, value?: object) {
        this.success = success || false
        this.value = value || {}
    }

    setResponse(success: boolean, value: object) {
        this.success = success
        this.value = value
    }

    getResponse() {
        return {
            success: this.success,
            value: this.value
        }
    }

}









