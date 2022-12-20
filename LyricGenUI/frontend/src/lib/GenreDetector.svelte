<script lang="ts">
    const genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"];

    let files: FileList;
    let result = null;

    async function predictGenre(file: File) {
        const formData = new FormData();
        formData.append("file", file);

        return await fetch("http://localhost:5000/genre", {
            method: "POST",
            body: formData,
        })
        .then(res => res.json());
    }

    $: if (files && files[0]) {
        result = predictGenre(files[0]);
    }
</script>

<input accept="audio/*" bind:files type="file" />

{#if files && files[0]}
    {#await result}
        <p>Predicting...</p>
    {:then { result }}
        <p>The genre is {genres[result]}</p>
    {:catch error}
        <p class="text-red-600">{error.message}</p>
    {/await}
{/if}
