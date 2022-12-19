<script lang="ts">
    let files: FileList;

    $: if (files) {
        console.log("Hello files", files)
    }
</script>

<input
	accept="audio/*"
	bind:files
	type="file"
/>

{#if files}
	<p>Predicting...</p>
{/if}