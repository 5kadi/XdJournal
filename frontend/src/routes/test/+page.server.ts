import { PUBLIC_API_URL } from '$env/static/public'
import { apiFetch } from '$lib/api.js'
import type { PageServerLoad } from './$types.js'

export const load: PageServerLoad = async () => {
    return {
        message: new Promise((resolve) => setTimeout(() => resolve("Xd"), 1500))
    }
}