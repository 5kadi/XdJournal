
<script lang="ts">
	import { enhance } from "$app/forms";

    let { btnText } : { btnText: string } = $props()
</script>

<form method="POST" class="flex flex-col items-center" use:enhance>
    <h1>Username</h1>
    <input type="text" name="username">

    <h1>Password</h1>
    <input type="text" name="password">

    <button>{btnText}</button>
</form>

