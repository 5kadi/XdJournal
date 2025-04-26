<script lang="ts">
	import { enhance } from "$app/forms";
	import MediaField from "../media/MediaField.svelte";

	let { mediaContent = $bindable() } = $props()
    let formRef: HTMLFormElement, submitRef: HTMLButtonElement;

    function autoUpload() {
        formRef.requestSubmit(submitRef)
        formRef.classList.add('invisible')
    }

</script>


{#if mediaContent}
    <MediaField mediaUrl={mediaContent}/>
{:else}
    <div class="w-[30%] h-auto">
        <form method="POST" action="?/uploadMedia" bind:this={formRef} enctype="multipart/form-data" use:enhance>
            <input
                type="file"
                name="content"
                onchange={autoUpload}
            />
            <button class="invisible" type="submit" bind:this={submitRef}></button>
        </form>
    </div>
{/if}

