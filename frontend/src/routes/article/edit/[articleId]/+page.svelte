<script lang="ts">
	import { enhance } from "$app/forms";
    import ArticleField from "../../../../components/article/ArticleField.svelte";

    let { data, form } = $props()
    let articleContent = $state(data.success ? data.data.text_content : "")

</script>

{#if form}
    {#if form.success}
        <h2>{(form.data as any).message}</h2>
    {:else}
        <h2>{JSON.stringify(form.data)}</h2>        
    {/if}
{/if} 

<form method="POST" class="select-none flex flex-row gap-4" use:enhance>
    <button 
        formaction="?/save"
    >
        SAVE
    </button>
    <button>PUBLISH</button>
    <input type="hidden" name="id" value={data.data.id}/>
    <input type="hidden" name="text_content" value={articleContent}/>
</form>

<ArticleField bind:articleContent={articleContent}/>


