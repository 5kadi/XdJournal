<script lang="ts">
	import '../app.css';
	import UpperPopup from '../components/popups/UpperPopup.svelte';
	let { children } = $props();
</script>

{@render children()}

<UpperPopup/>
