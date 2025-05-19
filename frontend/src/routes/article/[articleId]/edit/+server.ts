import { apiFetch } from '$lib/api'

//for saving textBlocks & publishing articles
export const PATCH = async ({request, params, cookies}) => {
    const data = await request.json()
    const res = await apiFetch(
        `/article/${params.articleId}/`.concat(data.content_frag ? 'save_block' : 'publish') ,
        {
            method: "PATCH",
            body: JSON.stringify(data),
        },
        cookies.get('access')
    )

    return res
}

