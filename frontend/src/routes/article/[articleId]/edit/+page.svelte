<script lang="ts">
    import TextBlock from "../../../../components/articleEdit/TextBlock.svelte";
    import MediaBlock from "../../../../components/articleEdit/MediaBlock.svelte";
    import EditPopup from "../../../../components/articleEdit/EditPopup.svelte";
	import { upperPopupState } from "../../../../shared.svelte";
	import ArticleCard from "../../../../components/cards/ArticleCard.svelte";

    let { data, form } = $props()
    upperPopupState.message = form?.message

    let articleBlocks: Array<[string, {type: string, content: string}]> = $state(
        data.content.map(
            (block: {type: string, content: string}, idx: number) => [String(idx), block]
        )
    )

    function addBlock(type: string) {
        //probably shitty code but idgaf Xd
        const addedBlock = [String(articleBlocks.length), {type: type, content: ""}] as [string, {type: string, content: string}]
        articleBlocks = [...articleBlocks, addedBlock]   
    }

    async function publishArticle(publishStatus: boolean) {
        const res = await fetch(
            "?action=publish",
            {
                method: "PATCH",
                body: JSON.stringify({publish_status: publishStatus})
            }
        )
        const resData = await res.json()
        upperPopupState.message = resData.message
    }

    function deleteBlock(id: string) {
        articleBlocks = articleBlocks.filter( 
            (el) => el[0] !== id
        )
        articleBlocks = articleBlocks.map(
            (el, idx: number) => [String(idx), el[1]]
        )
        //console.log(articleBlocks.map((el) => el[1]))
    }
    
    const BLOCKS: {[key: string]: typeof TextBlock} = {
        "text": TextBlock,
        "media": MediaBlock
    }

</script>


<section>
    <button onclick={() => publishArticle(true)}>PUBLISH</button>
</section>
<main class="relative">
    <h1 class="font-bold text-2xl" contenteditable="true" bind:innerText={data.header}></h1>
    {#each articleBlocks as contentBlock, i (contentBlock[0])}
        {@const Block = BLOCKS[contentBlock[1].type]}
        <Block 
            bind:blockData={articleBlocks[i]}
            deleteFromArray={deleteBlock}
        />
    {/each}
</main>

<div class="flex flex-row gap-4">
    <button onclick={() => addBlock('text')}>Text Block +</button>
    <button onclick={() => addBlock('media')}>Media Block +</button>
</div>

<EditPopup/>




