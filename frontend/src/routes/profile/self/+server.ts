import { apiFetch } from '$lib/api.js'
import { setAuthCookies } from '$lib/auth.js'
import { json } from '@sveltejs/kit'


export const PATCH = async ({request, params, cookies, url}) => {
    //just make sure action exists and it's either "file" or "text" lmfao
    const action = url.searchParams.get('action') as "file" | "text"

    //shitty code ngl
    const userData = cookies.get('userData')
    if (!userData) return json({ message: "Failed to acquire userData" })
    const { id } = JSON.parse(userData)
    if (!id) return json({ message: "Failed to get user's id" })

    let res: any; //res always exists, otherwise this block couldn't be reached

    if (action == "file") {
        const formData = await request.formData()

        res = await apiFetch(
            `/auth/patch/${id}`,
            {
                method: "PATCH",
                body: formData
            },
            cookies.get('access'),
            false
        )
    } else if (action == "text") {
        const data = await request.json()
        //console.log(data)

        res = await apiFetch(
            `/auth/patch/${id}`,
            {
                method: "PATCH",
                body: JSON.stringify(data)
            },
            cookies.get('access')
        )
    }  
    //shitty code again
    const {message, ...newUserData} = await res.json()
    if (newUserData) setAuthCookies(cookies, { userData: JSON.stringify(newUserData) })
    return json({message, newUserData: newUserData})

}