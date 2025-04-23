
<script lang="ts">
	import { enhance } from "$app/forms";
	import type { HTMLInputTypeAttribute } from "svelte/elements";

    let { 
        fields,
        submitText,
        headerText
    } : 
    { 
        fields: {name: string, type: HTMLInputTypeAttribute}[],
        submitText: string
        headerText: string

    } = $props()

</script>

<form method="POST" class="flex flex-col items-center" use:enhance>
    <h1>{headerText}</h1>

    {#each fields as field (field.name)}
        <h2>{field.name}</h2>
        <input type={field.type} name={field.name.toLowerCase()}/>
    {/each}

    <button type="submit">{submitText}</button>
</form>



