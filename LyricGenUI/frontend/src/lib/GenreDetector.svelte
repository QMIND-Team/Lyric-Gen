<script lang="ts">
    let files: FileList;

    $: if (files) {
        console.log("Hello files", files);

        // const formData = new FormData();
        // formData.append("file", files.item(0));
        // fetch("http://localhost:5000/genre", {
        //     method: "POST",
        //     body: formData,
        // }).then(res => {
        //     console.log(res)
        // });

        fetch("http://localhost:5000/genre", {
            method: "POST",
        }).then(res => {
            console.log(res.body)
        });
    }
</script>

<input accept="audio/*" bind:files type="file" />

{#if files}
    <p>Predicting...</p>
{/if}
