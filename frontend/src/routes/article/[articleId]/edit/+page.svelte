<script lang="ts">
    import TextBlock from "../../../../components/article/TextBlock.svelte";
    import MediaBlock from "../../../../components/article/MediaBlock.svelte";
    import EditPopup from "../../../../components/article/EditPopup.svelte";
	import ErrorPopup from "../../../../components/errors/ErrorPopup.svelte";
    import { generateId } from "$lib/article";

    let { data, form } = $props()
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
</script>

{#if form}
    <ErrorPopup parentForm={form}/>
{/if} 


<main class="relative">
    {#await data}
        <h1>Loading...</h1>
    {:then res} 
        {#if res.success}
            <h1 class="font-bold text-2xl" contenteditable="true" bind:innerText={res.value.header}></h1>
            {#each Object.entries(res.value.content as {[id: string]: {type: string, content: string}}) as contentBlock (contentBlock[0])}
                {#if contentBlock[1].type === "text"} 
                    <TextBlock blockData={contentBlock}/>
                {:else if contentBlock[1].type === "media"}
                    <MediaBlock blockData={contentBlock}/>
                {/if}
            {/each}
        {:else}
            {JSON.stringify(res.value)}
        {/if}
    {/await}

    {#if addedBlock}
        {#if addedBlock[1].type === "text"} 
            <TextBlock blockData={addedBlock}/>
        {:else if addedBlock[1].type === "media"}
            <MediaBlock blockData={addedBlock}/>
        {/if}
    {/if}
</main>

<div class="flex flex-row gap-4">
    <button onclick={() => addBlock('text')}>Text Block +</button>
    <button onclick={() => addBlock('media')}>Media Block +</button>
</div>

<EditPopup/>




