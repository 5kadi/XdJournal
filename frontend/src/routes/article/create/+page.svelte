

<script lang="ts">
	import GenericForm from "../../../components/forms/GenericForm.svelte";
	import { upperPopupState } from "../../../shared.svelte";

    let { form } = $props()
    upperPopupState.message = form?.message

</script>

<GenericForm 
    submitText="Create" 
    headerText="Create an article!"
    fields={
        [
            {
                name: 'Header',
                type: 'text'
            }
        ]
    }
/>
