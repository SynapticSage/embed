# Embed CLI Tool

`embed` is a command-line tool for generating semantic embeddings from text using either the `sentence-transformers` library or OpenAI's embedding models. It supports various pre-trained models and provides options for customizing the output format and destination.

## Features

- Generate semantic embeddings from text input.
- Support for different pre-trained models from SentenceTransformers.
- Support for OpenAI's embedding models.
- Customizable output format using separators.
- Output results to a file or standard output.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/synapticsage/embed.git
    cd embed
    ```

2. Use the provided Makefile to install the `embed` command:

    ```sh
    make install
    ```

## Usage

### Basic Usage with SentenceTransformers

You can pipe text into the `embed` command and get the embeddings as output:

```sh
echo -e "This is an example sentence.\nAnother sentence for embedding." | embed
