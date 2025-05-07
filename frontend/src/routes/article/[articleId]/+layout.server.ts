import { apiFetch } from '$lib/api.js'
import { error, redirect } from '@sveltejs/kit'
import { ServerResponse } from '$lib/api.js'

export async function load({ params, cookies }) {
    const { articleId } = params
    const accessToken = cookies.get('access')

    let articleResponse = new ServerResponse()

    const res = await apiFetch(
        `/article/get/${articleId}`,
        {
            method: "GET"
        },
        accessToken
    )
    if (res.ok) {
        let articleData = await res.json()
        //articleData.content = JSON.parse(articleData.content)
        articleResponse.setResponse(true, articleData)
    } else {
        const errData = await res.json()
        if (res.status === 404) {
            //console.log(errData)
            throw error(404, errData.message)
        }
        articleResponse.setResponse(false, errData)
    }
    
    return articleResponse.getResponse()
}