<script lang="ts">
    import AuthForm from "../../../components/forms/AuthForm.svelte";
	import { upperPopupState } from "../../../shared.svelte";
    import type { PageProps } from "./$types";

    let { form }: PageProps = $props()
    upperPopupState.message = form?.message
</script>

<main class="flex flex-col items-center">
    <AuthForm btnText={'Log in'}/>
</main>

