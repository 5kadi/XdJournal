
<script lang="ts">
    //NOTE: this component will have some functionality that's different from GenericForm
	import { enhance } from "$app/forms";
	import { onAction } from "./Utils.svelte";

    let { btnText } : { btnText: string } = $props()


</script>

<form method="POST" class="flex flex-col items-center" use:enhance={() => onAction}>
    <h1>Username</h1>
    <input type="text" name="username">

    <h1>Password</h1>
    <input type="text" name="password">

    <button>{btnText}</button>
</form>

