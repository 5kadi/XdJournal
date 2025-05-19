import { apiFetch, ServerResponse } from "./api";


export async function formActionsFetch(
    url: string,
    method: string,
    request: Request,
    {
        accessToken, 
        onsuccess,
        onerror
    } :
    {
        accessToken?: string, 
        onsuccess?: (resJson: any) => void
        onerror?: (errJson: any) => void
    }
) {
    const formData = await request.formData()
    const requestBody = JSON.stringify(Object.fromEntries(formData))
    let formResponse = new ServerResponse()
    
    const res = await apiFetch(
        url,
        {
            method: method,
            body: requestBody
        },
        accessToken && accessToken
    )
    const resData = await res.json()

    if (res.ok) {
        onsuccess && onsuccess(resData)
    } else {
        onerror && onerror(resData)
    }

    return resData

}