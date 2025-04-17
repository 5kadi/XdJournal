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
            '/user/token/get',
            {
                method: "POST",
                body: requestBody
            }
        )
        if (res.ok) {
            const {access, refresh} = await res.json()
            cookies.set('access', access, {path: '/'})
            cookies.set('refresh', refresh, {path: '/'})
            formResponse.setResponse(true, {message: 'Logged in successfully!'})
        } else {
            const errData = await res.json()
            formResponse.setResponse(false, errData)
        }

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
