<script lang="ts">
    let { data } = $props()
</script>

{#await data}
    <h1>Loading...</h1>
{:then res} 
    <h1 class="font-bold text-2xl">{res.value.header}</h1>
    <h2>Author's id: {res.value.author}</h2>
    {@html res.value.text_content}
{/await}