<script lang="ts">
    import { upperPopupState } from "../../shared.svelte";
</script>

{#if upperPopupState.message}
    <div class="fixed z-50 inset-x-0 mx-auto top-2 h-auto max-w-[33%] bg-white opacity-70 shadow-md p-2 flex flex-row justify-between">
        <h2>{upperPopupState.message}</h2>        
        <button onclick={() => upperPopupState.message = undefined}>X</button>
    </div> 
{/if}