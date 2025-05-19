import { apiFetch } from '$lib/api.js'
import { error } from '@sveltejs/kit'


export async function load({ params, cookies }) {
    const { articleId } = params
    const accessToken = cookies.get('access')

    const res = await apiFetch(
        `/article/get/${articleId}`,
        {
            method: "GET"
        },
        accessToken
    )
    const resData = await res.json()
    
    if (!res.ok) {
        error(res.status, JSON.stringify(resData))
    }
    return resData
}