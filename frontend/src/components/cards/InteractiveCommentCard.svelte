<script lang="ts">
    import { PUBLIC_BACKEND_URL } from "$env/static/public";
	import LikeButton from "../buttons/LikeButton.svelte";

    let { commentData } : { commentData: CommentListData } = $props()

</script>

<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<div class="p-1 shadow-md flex flex-col h-fit">
    <div class="flex flex-row gap-4">
        <img 
            class="rounded-full object-cover object-center aspect-square h-12"
            src={PUBLIC_BACKEND_URL + commentData.user.avatar} 
            alt={PUBLIC_BACKEND_URL + commentData.user.avatar}
        />
        <div class="flex flex-col gap-1 w-full">
            <div class="flex flex-row justify-between">
                <h1 class="text-lg overflow-clip">{commentData.user.username}</h1>
                <h3 class="w-20 text-xs">{commentData.create_date.split('T')[0]}</h3>
            </div>
            <div class="h-fit" style="white-space: pre-line;">
                {commentData.content}
            </div>
        </div>
    </div>
    <footer class="row-span-1 text-xs">
        <LikeButton
            initialIsLiked={commentData.is_liked}
            initialLikeCount={commentData.like_count}
            serverRoute={`?action=comment&commentId=${commentData.id}`}
        />
    </footer>
</div>