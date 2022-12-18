<script lang="ts">
  import GenreDetector from "./lib/GenreDetector.svelte";
  import LyricGenerator from "./lib/LyricGenerator.svelte";
</script>

<main class="container text-center">
  <h1 class="font-bold text-3xl mt-5">AI Lyric Generation and Genre Detection</h1>
  <div class="mt-3">
    <h2 class="font-bold text-2xl">Genre Detection</h2>
    <GenreDetector />
  </div>
  <div class="mt-5">
    <h2 class="font-bold text-2xl">Lyric Generation</h2>
    <LyricGenerator />
  </div>
  <p class="mt-5">
    Do you have the musical talent of Freddie Mercury, but the lyrical talent of
    a sock?<br /><br />Fear no more—our team is building a deep learning
    algorithm to generate song lyrics given a key term and genre. Specifically,
    we will be using a recursive neural network for the lyric generation model,
    and a convolutional neural network for the genre detection model. The data
    we will use for our algorithm will be scraped from a dataset of songs and
    the Genius API. We are also planning to deploy a web API and web application
    that will interact with our lyric gen. algorithm.
  </p>
  <div class="mt-3">
    <!-- Team links -->
    <a href="https://github.com/QMIND-Team/Lyric-Gen" target="_blank" rel="noreferrer">GitHub</a>
    <a href="https://qmind.ca/" target="_blank" rel="noreferrer">QMIND</a>
    <a href="https://www.linkedin.com/in/jacobseiler/" target="_blank" rel="noreferrer">Jacob Seiler</a>
    <a href="https://www.linkedin.com/in/james-mccarron-1624aa182/" target="_blank" rel="noreferrer">James McCarron</a>
    <a href="https://www.linkedin.com/in/ted-brownlow-7043ab168/" target="_blank" rel="noreferrer">Ted Brownlow</a>
    <a href="https://www.linkedin.com/in/joshua-neizer-395ba7140/" target="_blank" rel="noreferrer">Joshua Neizer</a>
  </div>
</main>
