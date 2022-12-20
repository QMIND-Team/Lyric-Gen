<script lang="ts">
    let files: FileList;
    let result = null;

    async function predictGenre(file: File) {
        const formData = new FormData();
        formData.append("file", file);

        return await fetch("http://localhost:5000/genre", {
            method: "POST",
            body: formData,
        });
    }

    $: if (files && files[0]) {
        result = predictGenre(files[0]);
    }
</script>

<input accept="audio/*" bind:files type="file" />

{#if files && files[0]}
    {#await result}
        <p>Predicting...</p>
    {:then res}
        <p>The genre is {res}</p>
    {:catch error}
        <p class="text-red-600">{error.message}</p>
    {/await}
{/if}
