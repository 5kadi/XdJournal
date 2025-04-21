import type { Actions } from './$types';
import { formActionsFetch } from '$lib/forms';

//NOTE: there is no need for message on successful login or reqister
export const actions: Actions = {
    default: async ({cookies, request}) => formActionsFetch( 
        '/user/token/get',
        "POST",
        request,
        {
            onsuccess: (resJson: any) => {
                cookies.set('access', resJson.access, {path: '/'})
                cookies.set('refresh', resJson.refresh, {path: '/'})
            }
        }
    )
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
            cookies.set('refresh', refresh, {path: '/'})
        }
        else {
            console.log(resData)
        }
	}
} satisfies Actions;
*/
