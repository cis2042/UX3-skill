import os
import re
import pytest

def get_all_md_files():
    md_files = []
    for root, dirs, files in os.walk("."):
        # Skip .git and hidden dirs
        if '.git' in dirs:
            dirs.remove('.git')
        # Skip __pycache__ etc
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('__')]

        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.normpath(os.path.join(root, file)))
    return md_files

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    links = []

    # Standard Markdown links: [text](link) or ![alt](link)
    # This regex catches the path part of [text](path "title") or [text](path#anchor)
    md_links = re.findall(r'!?\[.*?\]\(([^)\s]+)(?:\s+".*?")?\)', content)
    # Filter for local file-like extensions
    md_links = [l for l in md_links if l.split('#')[0].lower().endswith(
        ('.md', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.zip', '.pdf')
    )]
    links.extend(md_links)

    # Backticked "links": `path/to/file.md`
    # We look for backticks containing something that ends in a common file extension and has no spaces.
    backtick_links = re.findall(r'`([^`\n\s]+\.(?:md|png|jpg|jpeg|gif|svg|webp|zip|pdf))`', content)
    links.extend(backtick_links)

    return links

@pytest.mark.parametrize("md_file", get_all_md_files())
def test_markdown_links(md_file):
    """
    Test that all local links in Markdown files point to existing files.
    """
    links = extract_links(md_file)
    base_dir = os.path.dirname(md_file)

    broken_links = []
    for link in links:
        # Skip external links
        if link.startswith(("http://", "https://", "mailto:", "tel:")):
            continue

        # Strip anchors for existence check
        clean_link = link.split('#')[0]

        # Resolve path relative to the file
        # We also handle paths that might be absolute to the repo root if they start with /
        if clean_link.startswith('/'):
            target_path = os.path.join(".", clean_link.lstrip('/'))
        else:
            target_path = os.path.join(base_dir, clean_link)

        target_path = os.path.normpath(target_path)

        if not os.path.exists(target_path):
            broken_links.append(link)

    assert not broken_links, f"File {md_file} has broken links: {', '.join(broken_links)}"
