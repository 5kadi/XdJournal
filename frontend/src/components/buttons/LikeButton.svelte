<script lang="ts">
	import { upperPopupState } from "../../shared.svelte";

    //boilerplate
    let { 
        customHandleLike, 
        serverRoute,
        initialIsLiked, 
        initialLikeCount

    } : 
    { 
        customHandleLike?: () => void, 
        serverRoute: string,
        initialIsLiked: boolean, 
        initialLikeCount: number
    } = $props()

    let isLiked = $state(initialIsLiked)
    let likeCount = $state(initialLikeCount)

    async function handleLike() {
        const method = isLiked ? "DELETE" : "POST"
        const res = await fetch(
            serverRoute,
            {
                method: method
            }
        )
        if (res.ok) {
            isLiked = !isLiked
            likeCount += -1 + Number(isLiked) * 2
        }
        else {
            const { message } = await res.json()
            upperPopupState.message = message
        }
    }

</script>

<div class="flex flex-row gap-2">
    <button
        onclick={ customHandleLike ? customHandleLike : handleLike }
        class={isLiked ? "text-red-400" : "text-black"}
    >
        Like
    </button>
    <text>{likeCount}</text>
</div>