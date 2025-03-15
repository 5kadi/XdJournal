import { redirect } from '@sveltejs/kit';



export async function load({ cookies }) {
    cookies.delete('access', {path: '/'})
    cookies.delete('refresh', {path: '/'})

    if (!(cookies.get('access') && cookies.get('refresh'))) { //theoretically i don't need it but i wont risk removing it
        redirect(302, '/') //302 because without it browser will cache redirect path and this whole load() function wont work
    }
}
