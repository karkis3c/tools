import sys
import urllib.parse
import argparse

def process_url(url):
    parsed_url = urllib.parse.urlparse(url)

    url_without_query = urllib.parse.urlunparse(
        (parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', '')
    )

    path_segments = parsed_url.path.strip('/').split('/')

    unique_urls = set()

    unique_urls.add(url_without_query)

    for i in range(len(path_segments), 0, -1):
        truncated_path = '/'.join(path_segments[:i])
        truncated_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{truncated_path}"
        unique_urls.add(truncated_url)

    return sorted(unique_urls)

def main(output_file=None):
    output_lines = []

    for line in sys.stdin:
        url = line.strip()
        if url:
            results = process_url(url)
            output_lines.extend(results)

    unique_output_lines = sorted(set(output_lines))

    if output_file:
        with open(output_file, 'w') as f:
            for line in unique_output_lines:
                f.write(line + '\n')
    else:
        for line in unique_output_lines:
            print(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Uri Cutter 🔪')
    parser.add_argument('-o', '--output', type=str, help='Output file to save the results "default:console"')
    args = parser.parse_args()

    main(output_file=args.output)
