import { tokenIsValid, refreshAccess, clearAuthCookies } from '$lib/auth.js'



export async function load({cookies}) { //subject to change
    const accessToken = cookies.get('access')
    const refreshToken = cookies.get('refresh')
    let accessIsValid, refreshIsValid

    if (accessToken) accessIsValid = tokenIsValid(accessToken)
    if (accessIsValid) return

    if (refreshToken) refreshIsValid = tokenIsValid(refreshToken)
    if (refreshIsValid) await refreshAccess(cookies, refreshToken!)

    if (!(accessIsValid && refreshIsValid)) {
        clearAuthCookies(cookies)
    }
}