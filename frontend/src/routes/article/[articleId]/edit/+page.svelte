<script lang="ts">
	import { enhance } from "$app/forms";
    import ArticleField from "../../../../components/article/ArticleField.svelte";

    let { data, form } = $props()
    let articleContent = $state(data.success ? data.value.text_content : "")

</script>

{#if form}
    {#await form}
        <h1>Loading...</h1>
    {:then res}
        {#if res.success}
            <h2>{(res.value as any).message}</h2>
        {:else}
            <h2>{JSON.stringify(res.value)}</h2>        
        {/if}
    {/await}
{/if} 

{#await data}
    <h1>Loading...</h1>
{:then res} 
    {#if res.success}
        <form method="POST" class="select-none flex flex-row gap-4" use:enhance>
            <button 
                formaction="?/save"
            >
                SAVE
            </button>
            <button
                formaction="?/publish"
            >PUBLISH
            </button>
            <input type="hidden" name="id" value={res.value.id}/>
            <input type="hidden" name="text_content" value={articleContent}/>
        </form>
        
        <ArticleField bind:articleContent={articleContent}/>
    {:else}
        <h1>{JSON.stringify(res)}</h1>
    {/if}
{/await}



