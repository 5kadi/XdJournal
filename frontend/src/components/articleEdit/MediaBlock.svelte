<script lang="ts">
	import { upperPopupState } from "../../shared.svelte";
	import { PUBLIC_BACKEND_URL } from "$env/static/public";

	let { 
        articleBlock = $bindable(),
        deleteFromArray
    }: 
    { 
        articleBlock: ArticleBlock,
        deleteFromArray: (id: number) => void
    } = $props()

    async function createMedia(e: any) {
        const file = e.target.files[0]
        if (file) {
            let requestBody = new FormData()
            requestBody.append('block_content', file) //cause I don't send block type
            requestBody.append('block_id', String(articleBlock.id))

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
                articleBlock.blockData.content = content
            }
            else upperPopupState.message = resJson  
        }
    }

    async function deleteMedia(e: any) {
        if (articleBlock.blockData.content === "") {
			deleteFromArray(articleBlock.id)
			return
		}

        const res = await fetch(
            '?action=media',
            {
                method: "DELETE",
                body: JSON.stringify({block_id: articleBlock.id}),
            }
        ) 

        const resJson = await res.json()
        if (res.ok) deleteFromArray(articleBlock.id)
        else upperPopupState.message = resJson.message  
    }

</script>


{#if articleBlock.blockData.content}
    <div class="w-[30%] h-auto relative">
        <img 
            class="w-full h-auto" 
            src={PUBLIC_BACKEND_URL + articleBlock.blockData.content} 
            alt={PUBLIC_BACKEND_URL + articleBlock.blockData.content}
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
