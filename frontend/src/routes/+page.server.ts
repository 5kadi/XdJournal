import { apiFetch } from "$lib/api";




export async function load() {
    const res = await apiFetch(
        '/article/list',
        {
            method: "GET"
        }
    )
    const resData = await res.json()
    return {articleDataArr: resData}
}