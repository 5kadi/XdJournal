<script lang="ts">
    import { caretSpanEscape, wrapContent } from "./Utils";

	let { textContent = $bindable() } = $props()
	let editableDivRef: HTMLDivElement;

    //wrapContent inserts html tags into range and doesn't trigger state update, this is why we need this function
	function updateContent() {
		textContent = editableDivRef.innerHTML
	}
	
	async function handleFocus(e: any) {
		const {innerHTML} = e.target
		const currentSelection = document.getSelection()
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
</script>



<div 
	class="h-auto w-full inline-block"  
	contenteditable="true" 
	onfocus={handleFocus}
    onmouseup={updateContent}
	bind:this={editableDivRef} 
	bind:innerHTML={textContent}
>
</div>


