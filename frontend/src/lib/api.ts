import { PUBLIC_API_URL } from "$env/static/public"


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









