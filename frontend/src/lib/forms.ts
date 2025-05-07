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
    if (res.ok) {
        const resJson = await res.json()
        onsuccess && onsuccess(resJson)
        formResponse.setResponse(true, resJson)
    } else {
        const errJson = await res.json()
        onerror && onerror(errJson)
        formResponse.setResponse(false, errJson)
    }

    return formResponse.getResponse()

}