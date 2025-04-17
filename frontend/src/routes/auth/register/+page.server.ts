import type { Actions } from './$types';
import { apiFetch } from '$lib/api';
import { Response } from '$lib/api.js';

//too lazy to make it follow DRY principle lmao
export const actions: Actions = {
    default: async ({cookies, request}) => {
        const userData = await request.formData()
        const requestBody = JSON.stringify(Object.fromEntries(userData))
        let formResponse = new Response()
        
        const res = await apiFetch(
            '/user/create',
            {
                method: "POST",
                body: requestBody
            }
        )
        if (res.ok) {
            const {access, refresh} = await res.json()
            cookies.set('access', access, {path: '/'})
            cookies.set('refresh', refresh, {path: '/'})
            formResponse.setResponse(true, {message: 'Created an account successfully!'})
        } else {
            const errData = await res.json()
            formResponse.setResponse(false, errData)
        }

        return formResponse.getResponse()
    }
}