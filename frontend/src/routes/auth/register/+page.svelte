<script lang="ts">
	import AuthForm from "../../../components/forms/AuthForm.svelte";
    import type { PageProps } from "./$types";

    let { form }: PageProps = $props()
</script>

<main class="flex flex-col items-center">
    <AuthForm btnText={'Register'}/>
   
    {#if form}
        {#if form.success}
            <h2>{(form.value as any).message}</h2>
        {:else}
            <h2>{JSON.stringify(form.value)}</h2>
        {/if}
    {/if} 
</main>