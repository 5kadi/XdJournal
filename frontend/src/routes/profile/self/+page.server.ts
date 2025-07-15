import { apiFetch } from '$lib/api';
import type { Cookies } from '@sveltejs/kit';
import { setAuthCookies } from '$lib/auth';



export async function load({cookies} : {cookies: Cookies}) {
    const res = await apiFetch(
        '/auth/data',
        {
            method: "GET",
        },
        cookies.get('access')
    )
    const userData = await res.json()
    setAuthCookies(cookies, { userData: JSON.stringify(userData) })

    return { userData: userData } as { userData: UserData}
}