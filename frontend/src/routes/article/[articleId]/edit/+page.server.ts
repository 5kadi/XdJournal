import { formActionsFetch } from '$lib/forms.js';
import { type Actions } from '@sveltejs/kit';
import { Response, apiFetch } from '$lib/api.js';
import { invalidate } from '$app/navigation';

export const actions: Actions = {
    save: async ({cookies, request}) => formActionsFetch(
        '/article/save',
        "PATCH",
        request,
        {
            accessToken: cookies.get('access')
        },
    ),
    publish: async ({cookies, request}) => formActionsFetch(
        '/article/publish',
        "PATCH",
        request,
        {
            accessToken: cookies.get('access')
        }
    ),
    uploadMedia: async ({cookies, request, params}) => {
        const formData = await request.formData()
        let formResponse = new Response()
        const { articleId } = params

        //const matches = request.url.match(/\/article\/(?<articleId>\d+)\/edit/)!
        //const { articleId } = matches.groups! 
        formData.append('article', articleId!)

        const res = await apiFetch(
            "/media/create",
            {
                method: "POST",
                body: formData,
                //headers: {'Content-Type': 'multipart/form-data;'}
            },
            cookies.get('access'),
            false
        )
        
        if (res.ok) {
            const resJson = await res.json()
            formResponse.setResponse(true, resJson)
        } else {
            const errJson = await res.json()
            formResponse.setResponse(false, errJson)
        }
        
        return formResponse.getResponse()
    }

}

export async function load({ parent }) {
    let res = await parent()

    if (!res.value.is_owner) {
        res = {
            success: false,
            value: {
                message: 'This article is owned by a different author!'
            }
        }

    }
    
    return res
}