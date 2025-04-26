<script lang="ts">
    let { parentForm } = $props()
    let isVisible = $state(true)
</script>

{#if isVisible}
   <div class="fixed z-50 inset-x-0 mx-auto top-2 h-auto max-w-[33%] bg-white opacity-70 shadow-md p-2 flex flex-row justify-between">
        {#await parentForm}
            <h1>Loading...</h1>
        {:then res}
            {#if res.success}
                <h2>{(res.value as any).message}</h2>
            {:else}
                <h2>{JSON.stringify(res.value.message)}</h2>        
            {/if}
            <button onclick={() => isVisible = false}>X</button>
        {/await} 
    </div> 
{/if}


