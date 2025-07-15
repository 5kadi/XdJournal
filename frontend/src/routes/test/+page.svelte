<script lang="ts">
    import { dndzone } from "svelte-dnd-action";
    let items = $state([
		{id: 0, name: "item11"},
		{id: 1, name: "item12"},
		{id: 2, name: "item13"},
		{id: 3, name: "item14"},
		{id: 4, name: "item15"},
		{id: 5, name: "item16"},
		{id: 6, name: "item17"}
	])
    function handleDnd(e: any) {
        items = e.detail.items;
    }
</script>

<div use:dndzone={{items: items, flipDurationMs:300}} onconsider="{handleDnd}" onfinalize="{handleDnd}">
    {#each items as item, i (item.id)}
        <div>{item.name}{i}</div>
    {/each}
</div>

