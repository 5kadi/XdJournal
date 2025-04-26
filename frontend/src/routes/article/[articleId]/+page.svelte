<script lang="ts">
	import MediaField from '../../../components/media/MediaField.svelte';

    let { data } = $props()
</script>

{#await data}
    <h1>Loading...</h1>
{:then res}
    <h1 class="font-bold text-2xl">{res.value.header}</h1>
    <h2>Author's id: {res.value.author}</h2>
    {#each res.value.content as contentBlock}
        {#if contentBlock.type === "text"} 
            <div>{@html contentBlock.content}</div>
        {:else if contentBlock.type === "media"}
            <MediaField mediaUrl={contentBlock.content}/>
        {/if}
    {/each}
{/await}