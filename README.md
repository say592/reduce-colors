# SVG Color Reducer

Reduce the number of colors in SVG files using K-Means clustering.

## Web Interface

A user-friendly web interface is available that runs entirely in your browser. No server or Python installation required!

### Try it Online

Visit the web interface: [https://say592.github.io/reduce-colors/](https://say592.github.io/reduce-colors/)

### Features

- 🎨 Upload SVG files via click or drag & drop
- 🔢 Specify the number of colors you want (1-256)
- 👀 Live preview of both original and reduced images
- 💾 Download the reduced SVG file
- 🚀 Runs completely client-side (no server needed)

### Hosting on GitHub Pages

1. Go to your repository settings
2. Navigate to "Pages" section
3. Under "Source", select the branch (usually `main` or `master`)
4. Select the root directory `/`
5. Click "Save"
6. Your web interface will be available at `https://YOUR-USERNAME.github.io/reduce-colors/`

## Python CLI Tool

For command-line usage or integration into other tools, use the Python script.

### Requirements

```bash
pip install scikit-learn svgpathtools
```

### Usage

```python
python reduce_colors.py
```

Edit the script to specify:
- `input_svg`: Path to your input SVG file
- `output_svg`: Path for the output file
- `n_colors`: Number of colors to reduce to

## How it Works

The tool uses K-Means clustering to analyze and reduce colors:

1. **Color Extraction**: Extracts all colors from the SVG file
2. **Clustering**: Groups similar colors using K-Means algorithm
3. **Replacement**: Replaces each original color with its cluster center
4. **Output**: Generates a new SVG with reduced colors

## Credits

Original Python implementation based on code from: https://advanced-stack.com/resources/how-to-reduce-color-count-in-a-svg-file.html

Web interface and JavaScript implementation created with Claude.
