<script lang="ts">
    import { wrapContent, caretSpanEscape } from './Utils';

    let showEditMenu = $state(false)

    // svelte-ignore non_reactive_update
    let pos = {x: 0, y: 0} //DOM updates after this value changes, so state is not needed
	
    // svelte-ignore non_reactive_update
        let currentSelection: Selection; //it will trigger error during the first handleFocus, but who tf cares Xd
        let editMenuRef: HTMLDivElement;


    function handleSelectionChange() {
        currentSelection = document.getSelection()!

    }

    function handleMouseUp(e: any) {
        
        const pointedElement = document.elementFromPoint(e.clientX, e.clientY)!
        if (!editMenuRef || !editMenuRef.contains(pointedElement)) { //NOTE: can use it to combine child spans later
            pos = {
                x: e.pageX + 5,
                y: e.pageY + 5
            } //updates first
        }

        //selection is always isCollapsed on the first mouse-up (focus), so EditMenu won't be shown
        if (
            currentSelection &&
            !currentSelection.isCollapsed
            //!(currentSelection.anchorOffset === currentSelection.focusOffset) //can remove i think
        ) {	
            showEditMenu = true //renders second
        }
        else {
            showEditMenu = false
        }
    }
    
    function handleEdit(cssClass: string) {
        wrapContent(currentSelection, cssClass) 
    }

</script>

{#if showEditMenu}
    <div 
		class="absolute z-30 shadow-lg rounded-md p-2 bg-white"
		style="top: {pos.y}px; left: {pos.x}px;"
		bind:this={editMenuRef}
	>
		<div>
			<button onclick={() => {handleEdit('font-bold')}}>Bold</button>
			<button onclick={() => {handleEdit('italic')}}>Cursive</button>
		</div>
	</div>
{/if}



<svelte:document onselectionchange={handleSelectionChange} onmouseup={handleMouseUp}/>