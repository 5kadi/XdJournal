import { apiFetch } from '$lib/api.js';
import { Response } from '$lib/api.js';
import type { Actions } from '@sveltejs/kit';

export const actions: Actions = {
    save: async ({cookies, request}) => {
        const articleData = await request.formData()
        const requestBody = JSON.stringify(Object.fromEntries(articleData))
        let formResponse = new Response()

        const res = await apiFetch(
            '/article/save',
            {
                method: "PATCH",
                body: requestBody
            },
            cookies.get('access')
        )

        if (res.ok) {
            const successData = await res.json()
            formResponse.setResponse(true, successData)
        } 
        else {
            const errData = await res.json()
            formResponse.setResponse(false, errData)
        }

        return formResponse.getResponse()
    }
}

export async function load({ params, cookies }) {
    const { articleId } = params
    let articleResponse = new Response()

    const res = await apiFetch(
        `/article/get/${articleId}`,
        {
            method: "GET"
        },
        cookies.get('access')
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