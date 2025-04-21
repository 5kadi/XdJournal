<script lang="ts">
    let { data } = $props()
</script>

{#await data}
    <h1>Loading...</h1>
{:then res} 
    <h1>Author's id: {res.value.author}</h1>
    {@html res.value.text_content}
{/await}