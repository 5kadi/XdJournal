import { goto } from "$app/navigation";
import { upperPopupState } from "../../shared.svelte";

export async function onAction({result, update} : {result: any, update: any}) {
    switch (result.type) {
        case ('success'): 
            upperPopupState.message = JSON.stringify(result.data.message)
            await update()
            break
        case ('redirect'): //possibly useless line xd
            goto(result.location)
            break
        default:
            break
    }
}