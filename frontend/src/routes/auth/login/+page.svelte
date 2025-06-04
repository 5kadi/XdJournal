<script lang="ts">
    import AuthForm from "../../../components/forms/AuthForm.svelte";
	import { upperPopupState } from "../../../shared.svelte";
    import type { PageProps } from "./$types";

    let { form }: PageProps = $props()
    upperPopupState.message = JSON.stringify(form?.message)
</script>

<main class="flex flex-col items-center">
    <AuthForm type={"login"}/>
</main>

