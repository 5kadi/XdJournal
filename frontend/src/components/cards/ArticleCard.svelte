<script>
	import MediaField from "../media/MediaField.svelte";
    import { PUBLIC_BACKEND_URL } from "$env/static/public";

    let { articleData } = $props()
</script>


<article class="p-1 shadow-md grid grid-rows-12 h-full w-full">
    <section class="row-span-11 h-full w-full overflow-clip">
        <div class="flex flex-row justify-between">
            <h1 class="text-xl overflow-clip">{articleData.author.username}</h1>
            <h3>{articleData.create_date.split('T')[0]}</h3>
        </div>
        {#if articleData.header_media}
            <div class="h-3/5 bg-gray-50 flex justify-center items-center">
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