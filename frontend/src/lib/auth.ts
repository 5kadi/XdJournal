import type { Cookies } from "@sveltejs/kit"
import { api } from "./api"
import { jwtDecode } from "jwt-decode"


export function setAuthHeaders(cookies: Cookies, accessToken: string) {
    //validity is already checked before this function call or the token is new
    cookies.set('access', accessToken, {path: '/'})
    api.defaults.headers.common.Authorization = `Bearer ${accessToken}`
}

export function clearAuthCookies(cookies: Cookies) {
    cookies.delete('access', {path: '/'})
    cookies.delete('refresh', {path: '/'})
}

export function tokenIsValid(token: string) {
    const tokenDecoded = jwtDecode(token)
    const tokenExpiration = tokenDecoded.exp!
    const currentTime = Date.now() / 1000 // 1000 because token.exp is in seconds
    if (tokenExpiration < currentTime) {
        return false
    }
    return true
}

export async function refreshAccess(cookies: Cookies, refreshToken: string) {
    //let refreshStatus = false
    await api.post(
        '/user/token/refresh',
        { refresh: refreshToken }
    )
    .then(
        res => {
            if (res.status === 200) {
                setAuthHeaders(cookies, res.data.access)
                //refreshStatus = true
            }
        }
    )
    //return refreshStatus
}
