<script lang="ts">
    import ArticleField from "../../../components/article/ArticleField.svelte";
    let articleContent = $state("")


    function handleSave() {
        console.log(articleContent)
    }

</script>

<div class="select-none">
   <button onclick={handleSave}>SAVE</button>
    <button>PUBLISH</button> 
</div>


<ArticleField bind:articleContent={articleContent}/>
{@html articleContent}


