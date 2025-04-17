import type { Cookies } from "@sveltejs/kit"
import { jwtDecode } from "jwt-decode"

export function setAccess(cookies: Cookies, accessToken: string) {
    //validity is already checked before this function call or the token is new
    cookies.set('access', accessToken, {path: '/'})
}

export function clearAuthCookies(cookies: Cookies) {
    cookies.delete('access', {path: '/'})
    cookies.delete('refresh', {path: '/'})
}

export function tokenIsValid(token: string) {
    const tokenDecoded = jwtDecode(token)
    const tokenExpiration = tokenDecoded.exp!
    const currentTime = Date.now() / 1000 // 1000 because token.exp is in miliseconds\
    if (tokenExpiration < currentTime) {
        return false
    }
    return true
}
