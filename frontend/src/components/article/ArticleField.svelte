<script lang="ts">
	import { replaceMarkdown } from "$lib/article";
	import { tick } from "svelte";
	import { caretSpanEscape, wrapContent } from "./ArticleField";
	
	//import type { DOMAttributes, SvelteDocumentAttributes } from "svelte/elements";

    let articleText = $state("") //make it bindable or something idk xd
    //let articleHTML = $derived(replaceMarkdown(articleText)) //TODO: make inputs safe
	let editableDiv: HTMLDivElement = $state()!



	function handleEdit(cssClass: string) {
		const selection = window.getSelection()!
		wrapContent(selection, cssClass)
	}

	function handleFocus(e: any) {
		const selection = window.getSelection()!
		const {innerHTML} = e.target
		if (selection.isCollapsed && innerHTML && (innerHTML[innerHTML.length - 1] !== ";")) { //'&nbsp;', so ';' is the last symbol lmao
			caretSpanEscape(selection, e.target)
		}
	}

</script>


<div 
	contenteditable="true"
	onfocus={handleFocus}
	bind:innerText={articleText}
	bind:this={editableDiv}
>
</div>

<button onclick={() => {handleEdit('font-bold')}}>Bold</button>
<button onclick={() => {handleEdit('italic')}}>Cursive</button>



