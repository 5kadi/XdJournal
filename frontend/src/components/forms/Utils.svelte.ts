import { goto } from "$app/navigation";
import { upperPopupState } from "../../shared.svelte";

export async function setPopup({result, update} : {result: any, update: any}) {
    switch (result.type) {
        case ('success'): 
            upperPopupState.message = result.data.message
            await update()
            break
        case ('redirect'):
            goto(result.location)
            break
        default:
            break
    }
}