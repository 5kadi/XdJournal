import { redirect } from '@sveltejs/kit';
import { clearAuthCookies } from '$lib/auth.js';



export async function load({ cookies }) {
    clearAuthCookies(cookies)

    if (!(cookies.get('access') && cookies.get('refresh'))) { //theoretically i don't need it but i wont risk removing it
        redirect(302, '/') //302 because without it browser will cache redirect path and this whole load() function wont work
    }
}
