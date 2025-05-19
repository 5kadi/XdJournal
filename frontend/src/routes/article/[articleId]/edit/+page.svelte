<script lang="ts">
    import TextBlock from "../../../../components/article/TextBlock.svelte";
    import MediaBlock from "../../../../components/article/MediaBlock.svelte";
    import EditPopup from "../../../../components/article/EditPopup.svelte";
    import { generateId } from "$lib/article";
	import { upperPopupState } from "../../../../shared.svelte";

    let { data, form } = $props()
    upperPopupState.message = form?.message
    let addedBlock: [string, {type: string, content: string}] | undefined = $state()

    function addBlock(type: string) {
        const id = generateId()
        addedBlock = [
            id,
            {
                type: type,
                content: ""
            }
        ]
    }

    async function publishArticle(publishStatus: boolean) {
        const res = await fetch(
            "",
            {
                method: "PATCH",
                body: JSON.stringify({publish_status: publishStatus})
            }
        )
        const resData = await res.json()
        upperPopupState.message = resData.message
    }
    
    const ADDED_BLOCKS: {[key: string]: typeof TextBlock} = {
        "text": TextBlock,
        "media": MediaBlock
    }

</script>


<section>
    <button onclick={() => publishArticle(true)}>PUBLISH</button>
</section>
<main class="relative">
    <h1 class="font-bold text-2xl" contenteditable="true" bind:innerText={data.header}></h1>
    {#each Object.entries(data.content as {[id: string]: {type: string, content: string}}) as contentBlock (contentBlock[0])}
        {#if contentBlock[1].type === "text"} 
            <TextBlock blockData={contentBlock}/>
        {:else if contentBlock[1].type === "media"}
            <MediaBlock blockData={contentBlock}/>
        {/if}
    {/each}

    {#if addedBlock}
        {@const Block = ADDED_BLOCKS[addedBlock[1].type]}
        <Block blockData={addedBlock}/>
    {/if}
</main>

<div class="flex flex-row gap-4">
    <button onclick={() => addBlock('text')}>Text Block +</button>
    <button onclick={() => addBlock('media')}>Media Block +</button>
</div>

<EditPopup/>




