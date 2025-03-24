<script lang="ts">
	import { tick } from "svelte";
	import { caretSpanEscape, wrapContent } from "./ArticleField";

	let pos = {x: 0, y: 0}
	
	let { articleContent = $bindable() } = $props()
	let editableDiv: HTMLDivElement = $state()!
	let showEditMenu = $state(false)
	let currentSelection: Selection = $state()! //it will trigger error during the first handleFocus, but who tf cares Xd

	//wrapContent inserts html tags into range and doesn't trigger state update, this is why we need this function
	function updateContent() {
		articleContent = editableDiv.innerHTML
	}

	async function handleFocus(e: any) {
		const {innerHTML} = e.target
		if (
			currentSelection?.isCollapsed && 
			innerHTML && 
			(innerHTML[innerHTML.length - 1] !== ";")//'&nbsp;', so ';' is the last symbol lmao
			//(innerHTML.substr(innerHTML.length - 4) !== '<br>') //no space after breakline NOTE:temporarily deprecated
		) { 
			caretSpanEscape(currentSelection, e.target)
			updateContent()
		}
	}

	function handleSelectionChange(e: any) {
		currentSelection = document.getSelection()!
		//console.log('showMenu')
		if (
			!currentSelection.isCollapsed &&
			!(currentSelection.anchorOffset === currentSelection.focusOffset)
		) {	
			showEditMenu = true
		}
		else {
			showEditMenu = false
		}
		
	}

	function handleMouseUp(e: any) {
		pos = {
			x: e.clientX + 10,
			y: e.clientY + 10
		}
		//console.log('posApplied')
	}

	function handleEditMenuClick(cssClass: string) {
		wrapContent(currentSelection, cssClass)
		updateContent()
	}

	//so, inline-block div somehow inserts <br> instead of <div> on enter

</script>


<div 
	class="inline-block h-auto w-full absolute"  
	contenteditable="true" 
	onfocus={handleFocus} 	
	bind:this={editableDiv} 
	bind:innerHTML={articleContent}
>
</div>
{#if (showEditMenu)}
	{@render EditMenu(pos.x, pos.y)}
{/if}


{#snippet EditMenu(posX: number, posY: number)}
	<div class={`select-none absolute z-10 shadow-lg p-2 bg-white`} style="top: {posY}px; left: {posX}px;">
		<div class="">
			<button onclick={() => {handleEditMenuClick('font-bold')}}>Bold</button>
			<button onclick={() => {handleEditMenuClick('italic')}}>Cursive</button>
		</div>
	</div>
{/snippet}

<svelte:document onselectionchange={handleSelectionChange} onmousemove={handleMouseUp}/>

