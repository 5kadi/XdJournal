<script>
	import { goto } from "$app/navigation";
    import { PUBLIC_BACKEND_URL } from "$env/static/public";

    let { articleData } = $props()
</script>


<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<article class="p-1 shadow-md grid grid-rows-12 h-full w-full cursor-pointer" onclick={() => goto(`/article/${articleData.id}`)}>
    <section class="row-span-11 h-full w-full overflow-clip">
        <div class="max-h-1/6 flex flex-row justify-between">
            <div class="flex flex-row gap-4">
                <img 
                    class="rounded-full object-cover object-center aspect-square"
                    src={PUBLIC_BACKEND_URL + articleData.user.avatar} 
                    alt={PUBLIC_BACKEND_URL + articleData.user.avatar}
                />
                <h1 class="text-xl overflow-clip">{articleData.user.username}</h1>
            </div>
            <h3 class="min-w-1/6 text-xs">{articleData.create_date.split('T')[0]}</h3>
        </div>
        {#if articleData.header_media}
            <div class="h-3/5 bg-gray-50 flex">
                <img
                    class="h-full w-full object-contain"
                    src={PUBLIC_BACKEND_URL + articleData.header_media} 
                    alt={PUBLIC_BACKEND_URL + articleData.header_media}
                />
            </div>
        {/if}
        <div class="flex flex-col w-full break-all">
            <h1 class="font-bold text-md">{articleData.header}</h1>
            <div class="text-xs break-all">
                {@html articleData.header_content}
            </div>
        </div>
    </section>
    <footer class="row-span-1 text-xs">
        Likes kinda, Reposts, etc... Xd
    </footer>
</article>