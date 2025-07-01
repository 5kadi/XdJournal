<script lang="ts">
	import { upperPopupState } from "../../shared.svelte";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";
	import { onDestroy } from "svelte";

	let { 
        blockData = $bindable(),
        deleteFromArray
    }: 
    { 
        blockData: [string, {type: string, content: string}],
        deleteFromArray: (id: string) => void
    } = $props()

    async function createMedia(e: any) {
        const file = e.target.files[0]
        if (file) {
            let requestBody = new FormData()
            requestBody.append('block_content', file) //cause I don't send block type
            requestBody.append('block_id', blockData[0])

            const res = await fetch(
                ``,
                {
                    method: "POST",
                    body: requestBody,
                    //headers: {}
                }
            ) 

            const resJson = await res.json()
            if (res.ok) {
                const { content } = resJson
                blockData[1].content = content
            }
            else upperPopupState.message = resJson  
        }
    }

    async function deleteMedia(e: any) {
        if (blockData[1].content === "") {
			deleteFromArray(blockData[0])
			return
		}

        const res = await fetch(
            '?action=media',
            {
                method: "DELETE",
                body: JSON.stringify({block_id: blockData[0]}),
            }
        ) 

        const resJson = await res.json()
        if (res.ok) deleteFromArray(blockData[0])
        else upperPopupState.message = resJson.message  
    }

</script>


{#if blockData[1].content}
    <div class="w-[30%] h-auto relative">
        <img 
            class="w-full h-auto" 
            src={PUBLIC_BACKEND_URL + blockData[1].content} 
            alt={PUBLIC_BACKEND_URL + blockData[1].content}
        /> 
        <button 
            class="z-10 absolute right-0 top-0 p-2 m-0.5 rounded-md  bg-red-500 text-white font-bold"
            onclick={deleteMedia}
        >
            X
        </button>
    </div>
{:else}
    <div class="w-[30%] h-auto">
        <input 
            type="file"
            aria-label="Change avatar"
            onchange={createMedia}
        >
    </div>
{/if}
