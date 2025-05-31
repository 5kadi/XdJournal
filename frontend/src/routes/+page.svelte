<script>
	import ArticleCard from '../components/cards/ArticleCard.svelte';

    let { data } = $props()
</script>

<section class="grid grid-cols-3 grid-rows-2 gap-4 w-[70vw] h-[75vh]">
    {#each data.articleDataArr as articleData (articleData.id) }
        <ArticleCard articleData={articleData}/>
    {/each}
</section>



