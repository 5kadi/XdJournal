
<script lang="ts">
    //NOTE: this component will have some functionality that's different from GenericForm
	import { enhance } from "$app/forms";
	import { onAction } from "./Utils.svelte";

    let { type } : { type: "register" | "login" } = $props()
    let btnText = type.charAt(0).toUpperCase() + type.slice(1)


</script>

<form method="POST" class="flex flex-col items-center" use:enhance={() => onAction}>
    <h1>Email</h1>
    <input type="email" name="email"/>
    
    {#if type === "register"}
        <h1>Username</h1>
        <input type="text" name="username">
    {/if}


    <h1>Password</h1>
    <input type="text" name="password">

    <button>{btnText}</button>
</form>

