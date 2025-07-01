<script lang="ts">
	import { onDestroy, type Snippet } from "svelte";

    let { 
        scrollbarContent, 
        loadFunction,
        cssClass 
    }: 
    { 
        scrollbarContent: Snippet, 
        loadFunction: () => void
        cssClass?: string 
    } = $props()

    let scrollbarRef: HTMLElement;

    async function handleScroll(e: any) {
        const commentsRect = scrollbarRef.getBoundingClientRect()

        const scrollWindowHeight = window.screen.height
        const commentSectionHeight = commentsRect.height
        const commentSectionTop = -1 * commentsRect.top

        //basically, if there is not enough comments in the next window position, it loads more comments
        if (scrollWindowHeight + commentSectionTop >= commentSectionHeight) { 
            loadFunction()
        }
    } 

    onDestroy(
        () => {
            return () => {
                document.removeEventListener('onscroll', handleScroll)
            }
        }
    )

</script>


<section 
    class={ cssClass || "" }
    bind:this={scrollbarRef}
>
    {@render scrollbarContent()}
</section>

<svelte:document onscroll={handleScroll}/>