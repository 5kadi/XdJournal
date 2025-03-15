import type { Actions } from './$types';
import { api } from '$lib/api';
import { setAuthHeaders } from '$lib/auth';
import { FormResponse } from '$lib/forms';

//too lazy to make it follow DRY principle lmao
export const actions: Actions = {
    default: async ({cookies, request}) => {
        const userData = await request.formData()
        let formResponse = new FormResponse()

        await api.post( //await is needed to avoid broken pipe error
            '/user/create', 
            userData
        )
        .then(
            res => {
                if (res.status === 201) {
                    setAuthHeaders(cookies, res.data.access)
                    cookies.set('refresh', res.data.refresh, {path: '/'})
                    formResponse.setResponse(true, { message: 'Registered successfully!' })
                }
            }
        )
        .catch(
            err => {
                formResponse.setResponse(false, err.response.data)
            }
        )

        return formResponse.getResponse()
    }
}