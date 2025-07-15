import { apiFetch } from '$lib/api.js'
import { error } from '@sveltejs/kit'

//article data is needed for both editing and viewing
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

    let articleData = resData
    articleData.content = articleData.content.map(
        (el: {type: string, content: string}, i: number) => { return { id: i, blockData: el } }
    )

    return { articleData: articleData} as { articleData: ArticleData }
}