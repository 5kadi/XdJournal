<script lang="ts">
	import MediaBlock from "./MediaBlock.svelte";
	import TextBlock from "./TextBlock.svelte";
	import EditPopup from "./EditPopup.svelte";

	let { articleContent = $bindable() } : {articleContent: {type: string, content: string}[]} = $props()
	//let blocksLength = $state(articleContent.length)

	function addBlock(type: string) {
		articleContent = [...articleContent, {type: type, content: ""}]
	}
	//so, inline-block div somehow inserts <br> instead of <div> on enter
</script>

<main class="relative">
	{#each articleContent as contentBlock }
		{#if contentBlock.type === "text"} 
			<TextBlock bind:textContent={contentBlock.content}/>
		{:else if contentBlock.type === "media"}
			<MediaBlock bind:mediaContent={contentBlock.content}/>
		{/if}
	{/each}
</main>

<div class="flex flex-row gap-4">
	<button onclick={() => addBlock('text')}>Text Block +</button>
	<button onclick={() => addBlock('media')}>Media Block +</button>
</div>

<EditPopup/>







