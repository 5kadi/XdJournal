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
            '/user/token/get', 
            userData
        )
        .then(
            res => {
                if (res.status === 200) {
                    setAuthHeaders(cookies, res.data.access)
                    cookies.set('refresh', res.data.refresh, {path: '/'})
                    formResponse.setResponse(true, { message: 'Logged in successfully!' })
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

/*
export const actions = {
	default: async ({cookies, request, fetch}) => {
        const data = await request.formData()

        console.log(request.headers)
        const res = await fetch(
            '/user/token/get',
            {
                method: "POST",
                body: data,
                headers: request.headers
            }
        )
        const resData = await res.json()
        console.log(resData)

        if (res.status === 200) {
            const {access, refresh} = resData
            console.log(access, refresh)
            cookies.set('access', access, {path: '/'})
            cookies.set('refresh', access, {path: '/'})
        }
        else {
            console.log(resData)
        }
	}
} satisfies Actions;
*/
