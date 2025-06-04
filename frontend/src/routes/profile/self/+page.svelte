<script lang="ts">
    import { PUBLIC_BACKEND_URL } from "$env/static/public";
	import { upperPopupState } from "../../../shared.svelte";

    let { data }: {data: any} = $props()
    let userData = $state(data)

    async function changeAvatar(e: any) {
        const file = e.target.files[0]
        if (file) {
            let requestBody = new FormData()
            requestBody.append('avatar', file)

            const res = await fetch(
                '?type=file',
                {
                    method: "PATCH",
                    body: requestBody,
                    //headers: {}
                }
            ) 
            const {message, newUserData} = await res.json()
            upperPopupState.message = message

            if (newUserData) {
                userData = newUserData //customAvatar is not changed, so image doesn't rerender lmao
            }
        }

    }

</script>

<main class="w-full h-screen flex flex-row">
    <section class="w-1/5 h-screen flex flex-col fixed p-2">
        <div class="w-2/3 p-2">
            <img 
                class="rounded-full object-cover object-center aspect-square"
                src={PUBLIC_BACKEND_URL + userData.avatar} 
                alt={PUBLIC_BACKEND_URL + userData.avatar}
            >
            <input 
                type="file"
                aria-label="Change avatar"
                onchange={changeAvatar}
            >
        </div>

        <div class="flex flex-col w-full">
            <h1 class="text-lg overflow-clip font-bold">{userData.username}</h1>
            <h3 class="text-md overflow-clip">Email: {userData.email}</h3>
            <h3 class="text-md v">Status: {userData.is_active ? "active" : "banned"}</h3>
        </div>
    </section>
</main>