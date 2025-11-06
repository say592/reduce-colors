from sklearn.cluster import KMeans
from svgpathtools import svg2paths, wsvg


def extract_colors(paths, attrs):
    colors = []
    for attr in attrs:
        if 'fill' in attr:
            color = attr['fill']
            if color.startswith('#'):
                r, g, b = (
                    int(color[1:3], 16),
                    int(color[3:5], 16),
                    int(color[5:7], 16),
                )
                colors.append([r, g, b])
    return colors


def replace_colors(paths, attrs, kmeans):
    new_attrs = []
    for attr in attrs:
        new_attr = attr.copy()
        if 'fill' in attr:
            color = attr['fill']
            if color.startswith('#'):
                r, g, b = (
                    int(color[1:3], 16),
                    int(color[3:5], 16),
                    int(color[5:7], 16),
                )
                new_color = kmeans.predict([[r, g, b]])
                new_color_hex = '#{:02x}{:02x}{:02x}'.format(
                    int(kmeans.cluster_centers_[new_color][0][0]),
                    int(kmeans.cluster_centers_[new_color][0][1]),
                    int(kmeans.cluster_centers_[new_color][0][2]),
                )
                new_attr['fill'] = new_color_hex
        new_attrs.append(new_attr)
    return new_attrs


def reduce_colors(input_svg, output_svg, n_colors):
    paths, attrs = svg2paths(input_svg)
    colors = extract_colors(paths, attrs)
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(colors)
    new_attrs = replace_colors(paths, attrs, kmeans)
    wsvg(paths, attributes=new_attrs, filename=output_svg)


input_svg = 'input.svg'
output_svg = 'ouput.svg'
n_colors = 8

reduce_colors(input_svg, output_svg, n_colors)
