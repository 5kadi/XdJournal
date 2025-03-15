import { accessIsValid, refreshAccess } from '$lib/auth.js'



export async function load({cookies}) {
    const accessToken = cookies.get('access')
    if (accessToken) {
        const accessValidity = accessIsValid(accessToken) 
        if (accessValidity) {
            return
        }
        else {
            const refreshToken = cookies.get('refresh')
            if (refreshToken) await refreshAccess(cookies, refreshToken) //await to set cookies before response is generated
        }
    }
}