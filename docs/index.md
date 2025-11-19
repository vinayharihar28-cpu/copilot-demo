<!--
Copilot Demo Project - Documentation

Purpose
- Small demo library to help generate, render and serve simple documentation sites from Markdown sources.
- Intended for learning and experimenting with Copilot-style workflows.

Quick start
1. Install project dependencies (e.g., npm install).
2. Place your Markdown files in the docs/ directory.
3. Use the API to build or serve the documentation.

Public API (example function names)
- init(options)
    - Initialize the project environment.
    - options: { docsDir?: string, outDir?: string, template?: string }

- loadDocs(path)
    - Load and parse Markdown documents from the given path.
    - Returns an array of document objects: { path, content, metadata }

- render(doc, opts)
    - Render a parsed document to HTML.
    - opts may include template data and rendering options.

- build(options)
    - Build the full static site into the output directory.
    - options: { docsDir?: string, outDir?: string }

- serve(port, options)
    - Start a local static server for the built site (useful for preview).
    - Returns a server instance with a stop() method.

Example usage (Node/ES module)
- This demonstrates typical flows: initialize, load docs, build, and serve.

# Copilot Demo Project

This is the documentation for my Copilot demo.

## Usage
