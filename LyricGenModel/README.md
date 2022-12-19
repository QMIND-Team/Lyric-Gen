# AI Lyric Generation and Genre Detection

Created by Jacob Seiler, James McCarron, Ted Brownlow, and Joshua Neizer.

Do you have the musical talent of Freddie Mercury, but the lyrical talent of a sock?

Fear no more—our team is building a deep learning algorithm to generate song lyrics given a key term and genre. Specifically, we will be using a recursive neural network for the lyric generation model, and a convolutional neural network for the genre detection model. The data we will use for our algorithm will be scraped from a dataset of songs and the [Genius API](https://genius.com/developers). We are also planning to deploy a web API and web application that will interact with our lyric gen. algorithm.

## To run `Genre Classification`

1. Copy the `genres` folder from the [`GTZAN`](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification) dataset into the root of this project.

    > You can skip this step if you are running the code from the `Import data from CSV` step

1. Create a virtual environment of Python 3.8.9 (optional)

    > Note: If you get a `Could not install packages due to an OSError`, you will need to follow these steps: <https://stackoverflow.com/questions/64278198/error-can-not-perform-a-user-install-user-site-packages-are-not-visible-in>

1. Install all dependencies from `requirements.txt`
1. Run the notebook `Genre Classification.ipynb`.
