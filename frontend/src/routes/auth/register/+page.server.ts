import type { Actions } from './$types';
import { formActionsFetch } from '$lib/forms';
import { setAuthCookies } from '$lib/auth';
import { redirect } from '@sveltejs/kit';

//NOTE: there is no need for message on successful login or reqister
export const actions: Actions = {
    default: async ({cookies, request}) => formActionsFetch( 
        '/auth/create',
        "POST",
        request,
        {
            onsuccess: (resJson: any) => {
                setAuthCookies(
                    cookies, 
                    {
                        access: resJson.access,
                        refresh: resJson.refresh,
                        userData: JSON.stringify(resJson.userData)
                    }
                )
                redirect(302, '/profile/self')
            }
        }
    )
}
