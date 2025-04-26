<script lang="ts">
	import { enhance } from "$app/forms";
    import ArticleField from "../../../../components/article/ArticleField.svelte";
	import ErrorPopup from "../../../../components/errors/ErrorPopup.svelte";

    let { data, form } = $props()
    let articleContent = $state(data.success ? data.value.content : "")
    let articleHeader = $state(data.value.header)

</script>

{#if form}
    <ErrorPopup parentForm={form}/>
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
            >
                PUBLISH
            </button>
            <input type="hidden" name="id" value={res.value.id}/>
            <input type="hidden" name="header" value={articleHeader}/>
            <input type="hidden" name="content" value={JSON.stringify(articleContent)}/>
        </form>
        <h1 class="font-bold text-2xl" contenteditable="true" bind:innerText={articleHeader}></h1>
        <ArticleField bind:articleContent={articleContent}/>
    {:else}
        <h1>{JSON.stringify(res)}</h1>
    {/if}
{/await}



