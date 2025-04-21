import { apiFetch } from '$lib/api.js'
import { redirect } from '@sveltejs/kit'
import { Response } from '$lib/api.js'

export async function load({ params, cookies }) {
    const { articleId } = params
    const accessToken = cookies.get('access')

    let articleResponse = new Response()

    const res = await apiFetch(
        `/article/get/${articleId}`,
        {
            method: "GET"
        },
        accessToken
    )
    if (res.ok) {
        const articleData = await res.json()
        articleResponse.setResponse(true, articleData)
    } else {
        const errData = await res.json()
        articleResponse.setResponse(false, errData)
    }
    
    return articleResponse.getResponse()
}