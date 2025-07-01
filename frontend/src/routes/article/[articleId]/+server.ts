import { apiFetch } from '$lib/api.js'

export const GET = async ({request, params, url}) => {
    //just make sure it exists... again...
    const nextPage = url.searchParams.get('nextPage') 
    
    const res = await apiFetch(
        `/comment/${params.articleId}/list?page=${nextPage}` ,
        {
            method: "GET",
        }
    )

    return res
}