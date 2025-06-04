import { apiFetch } from '$lib/api.js'
import { setAuthCookies } from '$lib/auth.js'
import { json } from '@sveltejs/kit'


export const PATCH = async ({request, params, cookies, url}) => {
    const type: "file" | "text" | string | null = url.searchParams.get('type') //just make sure type exists lmfao


    //shitty code ngl
    const userData = cookies.get('userData')
    if (!userData) return json({ message: "Failed to acquire userData" })
    const { id } = JSON.parse(userData)
    if (!id) return json({ message: "Failed to get user's id" })

    if (type == "file") {
        const formData = await request.formData()

        const res = await apiFetch(
            `/auth/update/${id}`,
            {
                method: "PATCH",
                body: formData
            },
            cookies.get('access'),
            false
        )

        //shitty code again
        const {message, ...newUserData} = await res.json()
        if (newUserData) setAuthCookies(cookies, { userData: JSON.stringify(newUserData) })
        return json({message, newUserData: newUserData})

    } else if (type == "text") {

    }  


}