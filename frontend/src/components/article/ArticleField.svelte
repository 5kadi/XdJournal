<script lang="ts">
	import MediaBlock from "./MediaBlock.svelte";
	import TextBlock from "./TextBlock.svelte";
	import EditPopup from "./EditPopup.svelte";
	import { generateId } from "$lib/article";

	let { resArticleContent } = $props()
	let articleContent: {[id: string]: {type: string, content: string} } = $state(resArticleContent)

	function addBlock(type: string) {
		const id = generateId()
		let newBlock = {} as any
		newBlock[id] = {
			type: type,
			content: ""
		}
		articleContent = {...articleContent, ...newBlock}
	}
	//so, inline-block div somehow inserts <br> instead of <div> on enter
</script>

<main class="relative">
	{JSON.stringify(resArticleContent)}<br>
	{JSON.stringify(articleContent)}
	{#each Object.entries(articleContent) as contentBlock }
		{#if contentBlock[1].type === "text"} 
			<TextBlock blockData={contentBlock}/>
		{:else if contentBlock[1].type === "media"}
			<MediaBlock blockData={contentBlock}/>
		{/if}
	{/each}
</main>

<div class="flex flex-row gap-4">
	<button onclick={() => addBlock('text')}>Text Block +</button>
	<button onclick={() => addBlock('media')}>Media Block +</button>
</div>

<EditPopup/>







