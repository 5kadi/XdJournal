import { apiFetch } from '$lib/api'

//for saving text blocks & publishing articles
export const PATCH = async ({request, params, cookies, url}) => {
    //just make sure type exists and it's either "file" or "text" lmfao
    const action: "save_block" | "delete_block" | "publish" | string | null = url.searchParams.get('action') 
    const data = await request.json()
    
    const res = await apiFetch(
        `/article/${params.articleId}/${action}` ,
        {
            method: "PATCH",
            body: JSON.stringify(data),
        },
        cookies.get('access')
    )

    return res
}

//for uploading media blocks. POST request makes sense, because we are sending it to /media/article path
export const POST = async ({request, params, cookies, url}) => {
    const formData = await request.formData()

    const res = await apiFetch(
        `/media/article/${params.articleId}/create`,
        {
            method: "POST",
            body: formData
        },
        cookies.get('access'),
        false
    )

    return res
}

//for deleting blocks
export const DELETE = async ({request, params, cookies, url}) => {
    //again, just make sure it exists and is either "article" or "media"
    const action: "article" | "media" | string | null = url.searchParams.get("action")
    const data = await request.json()

    if (action === "article") console.log('todo') //TODO xd
    else if (action === "media") {
        const res = await apiFetch(
            `/media/article/${params.articleId}/delete`,
            {
                method: "DELETE",
                body: JSON.stringify(data)
            },
            cookies.get('access')
        )
        return res
    }
}
