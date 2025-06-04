import { tokenIsValid, clearAuthCookies } from '$lib/auth.js'
import { apiFetch } from '$lib/api.js'

export async function load({cookies}) {
    let accessToken = cookies.get('access')
    let refreshToken = cookies.get('refresh')
    let accessIsValid, refreshIsValid

    if (accessToken) accessIsValid = tokenIsValid(accessToken)
    if (accessIsValid) return

    if (refreshToken) refreshIsValid = tokenIsValid(refreshToken)
    if (refreshIsValid) {
        const requestBody = JSON.stringify({refresh: refreshToken})
        const res = await apiFetch(
            '/auth/token/refresh',
            {
                method: "POST",
                body: requestBody
            }
        )
        
        if (res.ok) {
            const { access } = await res.json()
            cookies.set('access', access, {path: '/'})
            return
        }

    }
    if (!refreshIsValid && !accessIsValid) clearAuthCookies(cookies)
   
}