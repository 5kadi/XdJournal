<script lang="ts">
    import TextBlock from "../../../../components/articleEdit/TextBlock.svelte";
    import MediaBlock from "../../../../components/articleEdit/MediaBlock.svelte";
    import EditPopup from "../../../../components/articleEdit/EditPopup.svelte";
	import { upperPopupState } from "../../../../shared.svelte";
    import { dndzone } from "svelte-dnd-action";

    let { data, form } = $props()
    upperPopupState.message = form?.message

    let { articleData } = data
    let articleBlocks = $state(articleData.content)

    function refreshBlocks() {
        articleBlocks = articleBlocks.map(
            (el, idx: number) => { return { id: idx, blockData: el.blockData } }
        )
    }

    function addBlock(type: string) {
        //probably shitty code but idgaf Xd
        const addedBlock: ArticleBlock = { 
            id: articleBlocks.length, 
            blockData: { type: type, content: ""} 
        }
        articleBlocks = [...articleBlocks, addedBlock]   
    }

    function deleteBlock(id: number) {
        articleBlocks.splice(id, 1)
        refreshBlocks()
        //console.log(articleBlocks.map((el) => el[1]))
    }

    function handleDnd(e: any) {
        articleBlocks = e.detail.items
    }

    async function saveBlockReposition(e: any) {
        const initialPos = e.detail.info.id
        if (!(initialPos === e.detail.items[initialPos].id)) {
            const finalPos = articleBlocks.findIndex((value) => value.id === initialPos)
            const res = await fetch(
                "?action=reposition_block",
                {
                    "method": "PATCH",
                    body: JSON.stringify(
                        {
                            initial_pos: initialPos,
                            final_pos: finalPos
                        }
                    )
                }
            )
            const resData = await res.json()
            if (res.ok) {
                refreshBlocks()
            }
            else {
                upperPopupState.message = resData.message
            }
        }
        refreshBlocks() //won't work without this xd
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
    
    const BLOCKS: {[key: string]: typeof TextBlock} = {
        "text": TextBlock,
        "media": MediaBlock
    }

</script>


<section class="select-none">
    <button onclick={() => publishArticle(true)}>PUBLISH</button>
</section>
<main class="relative">
    <h1 class="font-bold text-2xl" contenteditable="true" bind:innerText={articleData.header}></h1>
    <div 
        use:dndzone={ { items: articleBlocks, flipDurationMs: 300 } } 
        onconsider="{handleDnd}" 
        onfinalize="{saveBlockReposition}"
    >
        {#each articleBlocks as { id, blockData }, i (id)}
            {@const Block = BLOCKS[blockData.type]}
            <div class="p-1">
                <Block 
                    bind:articleBlock={articleBlocks[i]}
                    deleteFromArray={deleteBlock}
                />
            </div>
        {/each}
    </div>

</main>

<div class="flex flex-row gap-4 select-none">
    <button onclick={() => addBlock('text')}>Text Block +</button>
    <button onclick={() => addBlock('media')}>Media Block +</button>
</div>

<EditPopup/>




