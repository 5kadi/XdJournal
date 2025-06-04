<script lang="ts">
	import { enhance } from "$app/forms";
	import MediaField from "../media/MediaField.svelte";

	let { blockData }: {blockData: [string, {type: string, content: string}]} = $props()
    // svelte-ignore non_reactive_update
        let formRef: HTMLFormElement, submitRef: HTMLButtonElement;

    function autoUpload() {
        formRef.requestSubmit(submitRef)
        formRef.classList.add('invisible')
    }

</script>


{#if blockData[1].content}
    <MediaField mediaUrl={blockData[1].content}/>
{:else}
    <div class="w-[30%] h-auto">
        <form method="POST" action="?/uploadMedia" bind:this={formRef} enctype="multipart/form-data" use:enhance>
            <input
                type="file"
                name="content"
                onchange={autoUpload}
                aria-label="Select and image"
            />
            <input
                type="hidden"
                name="frag_id"
                value={blockData[0]}
            />
            <button class="invisible" type="submit" bind:this={submitRef}></button>
        </form>
    </div>
{/if}
