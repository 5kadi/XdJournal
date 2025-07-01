<script lang="ts">
	import { generateId } from '$lib/article';
	import CommentCard from '../../../components/cards/CommentCard.svelte';
	import CommentForm from '../../../components/forms/CommentForm.svelte';
	import MediaField from '../../../components/media/MediaField.svelte';
	import InfiniteScrollbar from '../../../components/scrollbars/InfiniteScrollbar.svelte';
	import { upperPopupState } from '../../../shared.svelte';

    let { data, form } = $props()
    upperPopupState.message = JSON.stringify(form?.message)

    let { articleData } = data
    let commentsData = $state(data.commentsData)

    let commentsSectionRef: HTMLElement;

    async function loadMore() {
        if (commentsData.next) {
            const nextUrl = new URL(commentsData.next)
            const nextPage = nextUrl.searchParams.get('page')

            const res = await fetch(
                `?nextPage=${nextPage}`,
                {
                    method: "GET"
                }
            )
            if (res.ok) {
                const { next, results } = await res.json()
                commentsData.next = next
                commentsData.results = [...commentsData.results, ...results]
            }
            else {
                upperPopupState.message = 'Failed to load more comments!'
            }
        }
    }

</script>

<main class="mb-10 mx-5">
    <h1 class="font-bold text-2xl">{articleData.header}</h1>
    <h2>Author: {articleData.user}</h2>
    {#each articleData.content.map((el: {type: string, content: string}, i: number) => [String(i), el]) as contentBlock, i (i)}
        {#if contentBlock[1].type === "text"} 
            <div>{@html contentBlock[1].content}</div>
        {:else if contentBlock[1].type === "media"}
            <MediaField mediaUrl={contentBlock[1].content}/>
        {/if}
    {/each}
</main>

<section class="flex flex-col gap-4 mx-5 mb-10" bind:this={commentsSectionRef}>
    <h1 class="text-2xl font-bold">Comments</h1>
    <CommentForm/>
    <InfiniteScrollbar
        scrollbarContent={Comments}
        loadFunction={loadMore}
    />
</section>

{#snippet Comments()}
    {#each commentsData.results as commentData, i (i)}
        <CommentCard commentData={commentData}/>
    {/each} 
{/snippet}




