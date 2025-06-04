import type { Cookies } from "@sveltejs/kit"
import { jwtDecode } from "jwt-decode"

export function setAuthCookies(
    cookies: Cookies, 
    {
        access, 
        refresh, 
        userData
    } : 
    {
        access?: string, 
        refresh?: string, 
        userData?: string
    }
) {
    access && cookies.set('access', access, {path: '/'})
    refresh && cookies.set('refresh', refresh, {path: '/'})
    userData && cookies.set('userData', userData, {path: '/'})
}

export function clearAuthCookies(cookies: Cookies) {
    cookies.delete('access', {path: '/'})
    cookies.delete('refresh', {path: '/'})
    cookies.delete('userData', {path: '/'})
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
