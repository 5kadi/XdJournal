

<script lang="ts">
	import GenericForm from "../../../components/forms/GenericForm.svelte";

    let {form} = $props()
 
</script>

{#if form}
    {#await form}
        <h1>Loading...</h1>
    {:then res}
        {#if res.success}
            <h2>{(res.value as any).message}</h2>
        {:else}
            <h2>{JSON.stringify(res.value.message)}</h2>        
        {/if}
    {/await}
{/if}  

<GenericForm 
    submitText="Create" 
    headerText="Create an article!"
    fields={
        [
            {
                name: 'Header',
                type: 'text'
            }
        ]
    }
/>
