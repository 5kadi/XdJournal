import { formActionsFetch } from "$lib/forms";
import { redirect, type Actions } from "@sveltejs/kit";

//Some bad design here I think. Should've made direct api fetches on button click (???)
export const actions: Actions = {
    default: async ({cookies, request}) => formActionsFetch(
        '/article/create',
        "POST",
        request,
        {
            accessToken: cookies.get('access'),
            onsuccess: (resJson: any) => redirect(302, `/article/${resJson.id}/edit`)
        }
    )
}

