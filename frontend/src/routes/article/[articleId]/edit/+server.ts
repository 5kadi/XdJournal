import { apiFetch } from '$lib/api'


export const PATCH = async ({request, params, cookies}) => {
    const data = await request.json()

    const requestBody = {
        content_frag: data,
        article_id: params.articleId,
    }

    const res = await apiFetch(
        '/article/save_block',
        {
            method: "PATCH",
            body: JSON.stringify(requestBody)
        },
        cookies.get('access')
    )

    return res
}
