<script lang="ts">
    import { caretSpanEscape, wrapContent } from "./Utils";

	let { blockData }: {blockData: [string, {type: string, content: string}]} = $props()
	let editableDivRef: HTMLDivElement;

    //wrapContent inserts html tags into range and doesn't trigger state update, this is why we need this function
	function updateContent() {
		blockData[1].content = editableDivRef.innerHTML
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

	async function saveContent() {
		const res = await fetch(
			'',
			{
				method: "PATCH",
				body: JSON.stringify({content_frag: Object.fromEntries([blockData])}),
			}
		)
	}
</script>



<div 
	class="h-auto w-full inline-block"  
	contenteditable="true" 
	onfocus={handleFocus}
	onfocusout={saveContent}
    onmouseup={updateContent}
	bind:this={editableDivRef} 
	bind:innerHTML={blockData[1].content}
>
</div>



