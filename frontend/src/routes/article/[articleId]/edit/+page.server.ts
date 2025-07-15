
import { error, type Actions } from '@sveltejs/kit';
import { apiFetch } from '$lib/api.js';


export const actions: Actions = {
    uploadMedia: async ({cookies, request, params}) => {
        const formData = await request.formData()
        const { articleId } = params

        //const matches = request.url.match(/\/article\/(?<articleId>\d+)\/edit/)!
        //const { articleId } = matches.groups! 
        formData.append('article', articleId!)

        const res = await apiFetch(
            `/media/article/${articleId}/create`,
            {
                method: "POST",
                body: formData,
                //headers: {'Content-Type': 'multipart/form-data;'}
            },
            cookies.get('access'),
            false //won't work with standard headers for some reason lmao
        )
        const resData = await res.json()
        return resData
    }

}

export async function load({ parent }) {
    const { articleData } = await parent()
    if (!articleData.is_owner) error(401, "You don't own this article!")
    return { articleData: articleData } as { articleData: ArticleData }
}