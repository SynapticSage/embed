#!/usr/bin/env python
import sys
# import json
import click
from sentence_transformers import SentenceTransformer

@click.command()
@click.option('-m', '--model', default='all-MiniLM-L6-v2', help='Model to use for embeddings')
@click.option('-s', '--sep', default=None, help='Separator for output embeddings')
@click.option('--output', type=click.Path(), help='File to write the output')
def main(model, sep, output):
    # Load model
    model = SentenceTransformer(model)

    # Read input from stdin
    input_text = sys.stdin.read().strip()
    sentences = input_text.split('\n')

    # Generate embeddings
    embeddings = model.encode(sentences)

    # Prepare output
    if sep is not None:
        output_text = sep.join(" ".join(map(str, embedding)) for embedding in embeddings)
    else:
        output_text = "\n".join(" ".join(map(str, embedding)) for embedding in embeddings)

    # Write output to file if specified, otherwise print to stdout
    if output:
        with open(output, 'w') as f:
            f.write(output_text)
    else:
        print(output_text)

if __name__ == "__main__":
    main()
