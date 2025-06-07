<script lang="ts">
	import { upperPopupState } from "../../shared.svelte";
    import { caretSpanEscape } from "./Utils";

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

	async function patchContent(action: "save_block" | "delete_block") { 
		const res = await fetch(
			`?action=${action}`,
			{
				method: "PATCH",
				body: JSON.stringify(
					{
						block: action === "save_block" && blockData[1], 
						block_id: blockData[0]
					}
				),
			}
		)

		if (!res.ok) {
			const { message } = await res.json()
			upperPopupState.message = message
		}
	}

</script>




<!-- svelte-ignore a11y_no_static_element_interactions -->
<section class="relative">
	<button 
		class="z-10 absolute right-0 top-0 p-2 m-0.5 rounded-md  bg-red-500 text-white font-bold"
		onclick={() => patchContent("delete_block")}
	>
		X
	</button>
	<div 
		class="h-auto w-full inline-block"  
		contenteditable="true" 
		onfocus={handleFocus}
		onfocusout={() => patchContent("save_block")}
		onmouseup={updateContent}
		bind:this={editableDivRef} 
		bind:innerHTML={blockData[1].content}
	>
	</div>
</section>




