<script lang="ts">
	import { onDestroy } from "svelte";
	import { upperPopupState } from "../../shared.svelte";
    import { caretSpanEscape } from "./Utils";

	let { 
        blockData = $bindable(),
        deleteFromArray
    }: 
    { 
        blockData: [string, {type: string, content: string}],
        deleteFromArray: (id: string) => void
    } = $props()

    //wrapContent inserts html tags into range and doesn't trigger state update, this is why we need this function
	function updateContent(e: any) {
		blockData[1].content = e.target.innerHTML
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
			updateContent(e)
		}
	}

	async function saveBlock() {
		//console.log('saving...')
		if (blockData[1].content === "") return

		const res = await fetch(
			'?action=save_block',
			{
				method: "PATCH",
				body: JSON.stringify(
					{
						block: blockData[1], 
						block_id: blockData[0]
					}
				),
			}
		)	
		const resJson = await res.json()

		if (res.ok) {
			const { block_id, block } = resJson
			blockData = [String(block_id), block]
		}
		else {
			const { message } = resJson
			upperPopupState.message = message
		}

	}

	async function deleteBlock() {
		if (blockData[1].content === "") {
			deleteFromArray(blockData[0])
			return
		}

		const res = await fetch(
			'?action=delete_block',
			{
				method: "PATCH",
				body: JSON.stringify(
					{
						block_id: blockData[0]
					}
				),
			}
		)	

		if (!res.ok) {
			const { message } = await res.json()
			upperPopupState.message = message
		}
		else {
			deleteFromArray(blockData[0])
		}
	}

</script>


{#if blockData}
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<section class="relative">
		<button 
			class="z-10 absolute right-0 top-0 p-2 m-0.5 rounded-md  bg-red-500 text-white font-bold"
			onclick={deleteBlock}
		>
			X
		</button>
		<!-- svelte-ignore a11y_click_events_have_key_events -->
		<div 
			class="h-auto w-full inline-block"  
			contenteditable="true" 
			onfocus={handleFocus}
			onclick={saveBlock}
			onfocusout={saveBlock}
			onmouseup={updateContent}
			bind:innerHTML={blockData[1].content}
		>
		</div>
	</section>	
{/if}







