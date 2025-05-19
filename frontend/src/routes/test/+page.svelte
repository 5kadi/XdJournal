<script lang="ts">
    let {data} = $props()
    async function xd() {
        return new Promise(
            (resolve) => setTimeout(() => resolve({"message": "xd"}), 1500)
        )
    }
</script>

{#await data.message}
    <h1>Loading...</h1>
{:then res} 
    <h1>{res}</h1>
{/await}