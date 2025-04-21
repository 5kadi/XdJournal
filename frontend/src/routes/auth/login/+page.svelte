<script lang="ts">
    import AuthMenu from "../../../components/auth/AuthMenu.svelte";
    import type { PageProps } from "./$types";

    let { form }: PageProps = $props()
</script>

<main class="flex flex-col items-center">
    <AuthMenu btnText={'Log in'}/>

    {#if form}
        {#if form.success}
            <h2>{(form.value as any).message}</h2>
        {:else}
            <h2>{JSON.stringify(form.value)}</h2>        
        {/if}
    {/if} 
</main>
