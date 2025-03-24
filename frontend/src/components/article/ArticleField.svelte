<script lang="ts">
	import { caretSpanEscape, wrapContent } from "./ArticleField";

	//content (the only useful part Xd)
	let { articleContent = $bindable() } = $props()
	//interactivity
	// svelte-ignore non_reactive_update
		let pos = {x: 0, y: 0} //DOM updates after this value changes, so state is not needed
	let currentSelection: Selection = $state()! //it will trigger error during the first handleFocus, but who tf cares Xd
	let showEditMenu = $state(false)
	//refs
	let editableDivRef: HTMLDivElement;
	let editMenuRef: HTMLDivElement;


	//wrapContent inserts html tags into range and doesn't trigger state update, this is why we need this function
	function updateContent() {
		articleContent = editableDivRef.innerHTML
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
	}

	function handleMouseUp(e: any) {
		const pointedElement = document.elementFromPoint(e.clientX, e.clientY)!
		if (!editMenuRef?.contains(pointedElement)) { //NOTE: can use it to combine child spans later
			pos = {
				x: e.clientX + 5,
				y: e.clientY + 5
			} //updates first
		}

		if (
			currentSelection &&
			!currentSelection.isCollapsed &&
			!(currentSelection.anchorOffset === currentSelection.focusOffset)
		) {	
			showEditMenu = true //mounts second
		}
		else {
			showEditMenu = false
		}
	}

	function handleEditMenuClick(cssClass: string) {
		wrapContent(currentSelection, cssClass)
		updateContent()
	}

	//so, inline-block div somehow inserts <br> instead of <div> on enter
</script>


<div 
	class="inline-block h-auto w-full"  
	contenteditable="true" 
	onfocus={handleFocus} 	
	bind:this={editableDivRef} 
	bind:innerHTML={articleContent}
>
</div>

{#if (showEditMenu)}
	{@render EditMenu(pos.x, pos.y)}
{/if}


{#snippet EditMenu(posX: number, posY: number)}
	<div 
		class="select-none absolute z-10 shadow-lg rounded-md p-2 bg-white"
		style="top: {posY}px; left: {posX}px;"
		bind:this={editMenuRef}
	>
		<div>
			<button onclick={() => {handleEditMenuClick('font-bold')}}>Bold</button>
			<button onclick={() => {handleEditMenuClick('italic')}}>Cursive</button>
		</div>
	</div>
{/snippet}

<svelte:document onselectionchange={handleSelectionChange} onmouseup={handleMouseUp}/>

