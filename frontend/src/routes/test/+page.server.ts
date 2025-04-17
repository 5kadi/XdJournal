import { PUBLIC_API_URL } from '$env/static/public'
import { apiFetch } from '$lib/api.js'

export async function load({cookies, fetch}) {
    const body = JSON.stringify(
        {
            username: 'xd',
            password: 'xdp'
        }
    )
    
    const res = await apiFetch(
        '/test',
        {
            method: "POST",
            body,   
        },
        cookies.get('access')
    )
    const data = await res.json()
    return data
}