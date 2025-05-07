<script lang="ts">
	import MediaField from '../../../components/media/MediaField.svelte';

    let { data } : {
        data: {
            success: boolean,
            value: {
                header: string,
                author: string,
                content: {
                    [id: string]: {
                        type: string,
                        content: string
                    }
                }
            }
        }
    } = $props()
</script>

{#await data}
    <h1>Loading...</h1>
{:then res}
    <h1 class="font-bold text-2xl">{res.value.header}</h1>
    <h2>Author's id: {res.value.author}</h2>
    {#each Object.entries(res.value.content) as contentBlock}
        {#if contentBlock[1].type === "text"} 
            <div>{@html contentBlock[1].content}</div>
        {:else if contentBlock[1].type === "media"}
            <MediaField mediaUrl={contentBlock[1].content}/>
        {/if}
    {/each}
{/await}