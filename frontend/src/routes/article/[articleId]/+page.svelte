<script lang="ts">
	import LikeButton from '../../../components/buttons/LikeButton.svelte';
	import InteractiveCommentCard from '../../../components/cards/InteractiveCommentCard.svelte';
	import CommentForm from '../../../components/forms/CommentForm.svelte';
	import MediaField from '../../../components/media/MediaField.svelte';
	import InfiniteScrollbar from '../../../components/scrollbars/InfiniteScrollbar.svelte';
	import { upperPopupState } from '../../../shared.svelte';

    let { data, form } = $props()
    upperPopupState.message = JSON.stringify(form?.message)

    let { articleData } = data
    let commentsData = $state(data.commentsData)

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
    <h2>Author: {articleData.user.username}</h2>
    {#each articleData.content as {id, blockData} (id)}
        {#if blockData.type === "text"} 
            <div>{@html blockData.content}</div>
        {:else if blockData.type === "media"}
            <MediaField mediaUrl={blockData.content}/>
        {/if}
    {/each}
</main>

<section class="flex flex-col gap-4 mx-5 mb-10"> 
    <div class="flex flex-row gap-4">
        <LikeButton 
            initialIsLiked={articleData.is_liked}
            initialLikeCount={articleData.like_count}
            serverRoute={"?action=article"}
        />  
        <h1 class="text-2xl font-bold">{articleData.comment_count} Comments</h1>
    </div> 
    <div>
        <CommentForm/>
        <InfiniteScrollbar
            scrollbarContent={Comments}
            loadFunction={loadMore}
        />
    </div>

</section>

{#snippet Comments()}
    {#each commentsData.results as commentData, i (i)}
        <InteractiveCommentCard commentData={commentData}/>
    {/each} 
{/snippet}




