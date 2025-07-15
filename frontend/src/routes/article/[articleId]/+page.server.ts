import { error, type Actions } from '@sveltejs/kit';
import { apiFetch } from '$lib/api.js';
import { formActionsFetch } from '$lib/forms.js';

export const actions: Actions = {
    default: async ({cookies, request, params}) => formActionsFetch( 
        `/comment/${params.articleId}/create`,
        "POST",
        request,
        {   
            accessToken: cookies.get('access'),
        }
    )
}

//loading comments is only needed for viewing 
export async function load({ params, parent, cookies }) {
    const { articleId } = params

    const res = await apiFetch(
        `/comment/${articleId}/list`,
        {
            method: "GET"
        },
        cookies.get('access')
    )
    const resData = await res.json()
    //console.log(resData)
    
    if (!res.ok) {
        error(res.status, JSON.stringify(resData))
    }
    //this object will be merged with response obj from +layout.server.ts
    return { commentsData: resData } as { commentsData: ArticleComments }
}