<script lang="ts">
    //NOTE: this component will have some functionality that's different from GenericForm
	import { enhance } from "$app/forms";
	import ResizingTextarea from "../inputs/ResizingTextarea.svelte";
	import { onAction } from "./Utils.svelte";

</script>

<form method="POST" class="flex flex-col gap-2" use:enhance={() => onAction}>
    <ResizingTextarea inputName={"content"}/>
    <button class="bg-blue-100 rounded-md" type="submit">Post</button>
</form>