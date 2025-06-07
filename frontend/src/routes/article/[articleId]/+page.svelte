<script lang="ts">
	import MediaField from '../../../components/media/MediaField.svelte';

    let { data } = $props()
</script>

<h1 class="font-bold text-2xl">{data.header}</h1>
<h2>Author: {data.user}</h2>
{#each data.content.map((el: {type: string, content: string}, i: number) => [String(i), el]) as contentBlock, i (i)}
    {#if contentBlock[1].type === "text"} 
        <div>{@html contentBlock[1].content}</div>
    {:else if contentBlock[1].type === "media"}
        <MediaField mediaUrl={contentBlock[1].content}/>
    {/if}
{/each}