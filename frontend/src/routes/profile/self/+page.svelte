<script lang="ts">
    import { PUBLIC_BACKEND_URL } from "$env/static/public";
	import { upperPopupState } from "../../../shared.svelte";
    import { fly } from "svelte/transition";

    let { data } = $props()
    let userData = $state(data.userData)

    let showButton = $state(false)

    async function changeAvatar(e: any) {
        const file = e.target.files[0]
        if (file) {
            let requestBody = new FormData()
            requestBody.append('avatar', file)

            const res = await fetch(
                '?action=file',
                {
                    method: "PATCH",
                    body: requestBody,
                    //headers: {}
                }
            ) 
            const {message, newUserData} = await res.json()
            upperPopupState.message = message

            if (newUserData) {
                userData = newUserData
            }
        }
    }

    async function changeUserData(valueKey: string) {
        const newValue = (userData as any)[valueKey]
        let requestBody: any =  {}
        requestBody[valueKey] = newValue

        const res = await fetch(
                '?action=text',
                {
                    method: "PATCH",
                    body: JSON.stringify(requestBody),
                    //headers: {}
                }
            ) 
            const {message, newUserData} = await res.json()
            upperPopupState.message = message

            if (newUserData) {
                userData = newUserData
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
            <div class="flex flex-col gap-1">
                <h1 
                    class="text-lg overflow-clip font-bold" 
                    contenteditable="true"
                    oninput={() => showButton = true}
                    bind:innerText={userData.username}
                ></h1>
                {#if showButton}
                    <div
                        class="w-full flex justify-center "
                        transition:fly={{y: -10, duration: 200}}
                    >
                        <button
                            class="w-full bg-blue-100 rounded-md"
                            onclick={() => changeUserData("username")}
                        >
                            Save
                        </button>
                    </div>
                {/if}
            </div>

            <h3 class="text-md overflow-clip">Email: {userData.email}</h3>
            <h3 class="text-md v">Status: {userData.is_active ? "active" : "banned"}</h3>
        </div>
    </section>
</main>