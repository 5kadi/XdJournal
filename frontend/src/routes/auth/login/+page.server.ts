import type { Actions } from './$types';
import { formActionsFetch } from '$lib/forms';
import { setAuthCookies } from '$lib/auth';
import { redirect } from '@sveltejs/kit';

//NOTE: there is no need for message on successful login or reqister
export const actions: Actions = {
    default: async ({cookies, request}) => formActionsFetch( 
        '/auth/token/get',
        "POST",
        request,
        {
            onsuccess: (resJson: any) => {
                setAuthCookies(
                    cookies, 
                    {
                        access: resJson.access,
                        refresh: resJson.refresh,
                        userData: JSON.stringify(resJson.userData)
                    }
                )
                redirect(302, '/profile/self')
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
