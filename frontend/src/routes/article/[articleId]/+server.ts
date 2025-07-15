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

export const POST = async ({request, params, url, cookies}) => {
    const action = url.searchParams.get('action') as "article" | "comment"

    let id = params.articleId
    if (action == "comment") {
        id = url.searchParams.get('commentId')!
    }

    const res = await apiFetch(
        `/like/${action}/${id}/set`,
        {
            method: "POST"
        },
        cookies.get('access')
    )

    return res
}

export const DELETE = async ({request, params, url, cookies}) => {
    const action = url.searchParams.get('action') as "article" | "comment"

    let id = params.articleId
    if (action == "comment") {
        id = url.searchParams.get('commentId')!
    }

    const res = await apiFetch(
        `/like/${action}/${id}/remove`,
        {
            method: "DELETE"
        },
        cookies.get('access')
    )

    return res
}