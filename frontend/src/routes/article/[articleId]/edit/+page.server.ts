import { formActionsFetch } from '$lib/forms.js';
import { redirect, type Actions } from '@sveltejs/kit';

export const actions: Actions = {
    save: async ({cookies, request}) => formActionsFetch(
        '/article/save',
        "PATCH",
        request,
        {
            accessToken: cookies.get('access')
        },
    ),
    publish: async ({cookies, request}) => formActionsFetch(
        '/article/publish',
        "PATCH",
        request,
        {
            accessToken: cookies.get('access')
        }
    )
}

export async function load({ cookies, parent }) {
    const accessToken = cookies.get('access')
    let res = await parent()

    if (!accessToken) {
        redirect(302, '/auth/login') //TODO: create a popup
    }

    if (!res.value.is_owner) {
        res = {
            success: false,
            value: {
                message: 'This article is owned by a different author!'
            }
        }

    }
    
    return res
}