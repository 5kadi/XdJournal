<script lang="ts">
    import { PUBLIC_BACKEND_URL } from "$env/static/public";
    let { mediaUrl } = $props()
</script>

<div class="w-[30%] h-auto">
    <img class="w-full h-auto" src={PUBLIC_BACKEND_URL + mediaUrl} alt={PUBLIC_BACKEND_URL + mediaUrl}/> 
</div>
