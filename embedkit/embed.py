#!/usr/bin/env python
import sys
import click
from sentence_transformers import SentenceTransformer

@click.command()
@click.option('-m', '--model', default='all-MiniLM-L6-v2', help='Model to use for embeddings')
@click.option('-s', '--sep', default=None, help='Separator for output embeddings')
@click.option('--output', type=click.Path(), help='File to write the output')
@click.option('--openai-api-key', envvar='OPENAI_API_KEY', help='OpenAI API key')
def main(model, sep, output, openai_api_key):
    # Determine which model to use
    if "openai" in model.lower():
        import openai
        # Check for API key
        if not openai_api_key:
            print("Error: OpenAI API key is required for OpenAI models.")
            sys.exit(1)
        
        # Set OpenAI API key
        openai.api_key = openai_api_key

        def get_embeddings(sentences):
            response = openai.Embedding.create(
                model=model,
                input=sentences
            )
            return [res['embedding'] for res in response['data']]
    else:
        # Load SentenceTransformers model
        model = SentenceTransformer(model)
        
        def get_embeddings(sentences):
            return model.encode(sentences)

    # Read input from stdin
    input_text = sys.stdin.read().strip()
    sentences = input_text.split('\n')

    # Generate embeddings
    embeddings = get_embeddings(sentences)

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
