import { formActionsFetch } from '$lib/forms.js';
import { type Actions } from '@sveltejs/kit';

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

export async function load({ parent }) {
    let res = await parent()

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