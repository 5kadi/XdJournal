<script lang="ts">

    let { inputName }: { inputName: string } = $props()

    function resize(e: any) {
        let textArea = e.target
        //textAreaRef.style.height = "auto"
        console.log(textArea.value)
        textArea.style.height = textArea.scrollHeight + 'px' //TODO: disable resizing on first input
    }

</script>

<textarea
    name={inputName}
    class="resize-none border-2 border-black rounded-md scrollbar-hidden"
    rows={1}
    oninput={resize}
>

</textarea>