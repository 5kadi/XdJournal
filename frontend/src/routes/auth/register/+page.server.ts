import type { Actions } from './$types';
import { formActionsFetch } from '$lib/forms';
import { upperPopupState } from '../../../shared.svelte';

//NOTE: there is no need for message on successful login or reqister
export const actions: Actions = {
    default: async ({cookies, request}) => formActionsFetch( 
        '/user/create',
        "POST",
        request,
        {
            onsuccess: (resJson: any) => {
                cookies.set('access', resJson.access, {path: '/'})
                cookies.set('refresh', resJson.refresh, {path: '/'})
            }
        }
    )
}
