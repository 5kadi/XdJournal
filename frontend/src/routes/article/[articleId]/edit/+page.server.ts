
import { type Actions } from '@sveltejs/kit';
import { ServerResponse, apiFetch } from '$lib/api.js';


export const actions: Actions = {
    uploadMedia: async ({cookies, request, params}) => {
        const formData = await request.formData()
        let formResponse = new ServerResponse()
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