#!/usr/bin/env python3
"""
Collect repository metadata and output as JSON.
Usage: python3 collect_repo_info.py [repo_path]
       Defaults to current directory if no path given.
"""
import json
import os
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'env',
               'dist', 'build', '.next', '.nuxt', 'coverage', '.cache'}
IGNORE_EXTS = {'.pyc', '.pyo', '.class', '.o', '.so', '.dll', '.exe',
               '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.woff',
               '.woff2', '.ttf', '.eot', '.min.js', '.min.css', '.lock'}

LANG_MAP = {
    '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
    '.tsx': 'TypeScript', '.jsx': 'JavaScript', '.vue': 'Vue',
    '.go': 'Go', '.rs': 'Rust', '.java': 'Java', '.kt': 'Kotlin',
    '.swift': 'Swift', '.rb': 'Ruby', '.php': 'PHP', '.cs': 'C#',
    '.cpp': 'C++', '.c': 'C', '.h': 'C/C++', '.sh': 'Shell',
    '.bash': 'Shell', '.zsh': 'Shell', '.html': 'HTML', '.css': 'CSS',
    '.scss': 'SCSS', '.sass': 'SASS', '.less': 'LESS', '.md': 'Markdown',
    '.json': 'JSON', '.yaml': 'YAML', '.yml': 'YAML', '.toml': 'TOML',
    '.sql': 'SQL', '.graphql': 'GraphQL', '.proto': 'Protobuf',
    '.dart': 'Dart', '.r': 'R', '.m': 'MATLAB', '.ex': 'Elixir',
    '.exs': 'Elixir', '.erl': 'Erlang', '.hs': 'Haskell',
    '.lua': 'Lua', '.tf': 'Terraform', '.dockerfile': 'Docker',
}


def run(cmd, cwd):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=15)
        return r.stdout.strip() if r.returncode == 0 else ''
    except Exception:
        return ''


def git_info(path):
    remote = run(['git', 'remote', 'get-url', 'origin'], path)
    branch = run(['git', 'branch', '--show-current'], path)
    if not branch:
        branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], path)
    description = run(['git', 'config', 'remote.origin.url'], path)

    log_raw = run(['git', 'log', '--pretty=format:%h|%an|%ae|%ad|%s',
                   '--date=short', '-20'], path)
    commits = []
    for line in log_raw.splitlines():
        parts = line.split('|', 4)
        if len(parts) == 5:
            commits.append({
                'hash': parts[0], 'author': parts[1],
                'email': parts[2], 'date': parts[3], 'message': parts[4]
            })

    total_commits = run(['git', 'rev-list', '--count', 'HEAD'], path)
    contributors_raw = run(['git', 'log', '--pretty=format:%an|%ae', '--no-duplicates'], path)
    contributors = []
    seen = set()
    for line in contributors_raw.splitlines():
        parts = line.split('|', 1)
        if parts and parts[0] not in seen:
            seen.add(parts[0])
            contributors.append({'name': parts[0], 'email': parts[1] if len(parts) > 1 else ''})

    first_commit_date = run(['git', 'log', '--pretty=format:%ad', '--date=short',
                              '--reverse', '-1'], path)
    last_commit_date = run(['git', 'log', '--pretty=format:%ad', '--date=short', '-1'], path)

    tags = run(['git', 'tag', '--sort=-version:refname', '-l'], path).splitlines()[:5]

    return {
        'remote_url': remote,
        'current_branch': branch,
        'total_commits': int(total_commits) if total_commits.isdigit() else 0,
        'recent_commits': commits,
        'contributors': contributors[:10],
        'first_commit_date': first_commit_date,
        'last_commit_date': last_commit_date,
        'tags': tags,
    }


def file_tree(root, max_depth=4):
    """Build a nested file tree dict, skipping ignored dirs."""
    tree = []

    def walk(dir_path, depth):
        if depth > max_depth:
            return []
        entries = []
        try:
            items = sorted(Path(dir_path).iterdir(),
                           key=lambda p: (p.is_file(), p.name.lower()))
        except PermissionError:
            return []
        for item in items:
            if item.name.startswith('.') and item.name not in {'.env.example', '.github'}:
                continue
            if item.name in IGNORE_DIRS:
                continue
            if item.is_dir():
                children = walk(item, depth + 1)
                entries.append({'name': item.name, 'type': 'dir', 'children': children})
            elif item.is_file():
                if item.suffix.lower() in IGNORE_EXTS:
                    continue
                size = item.stat().st_size
                entries.append({'name': item.name, 'type': 'file',
                                 'ext': item.suffix.lower(), 'size': size})
        return entries

    return walk(root, 0)


def language_stats(root):
    stats = defaultdict(lambda: {'files': 0, 'lines': 0})
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in IGNORE_DIRS and not d.startswith('.')]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            ext = fpath.suffix.lower()
            if ext in IGNORE_EXTS:
                continue
            lang = LANG_MAP.get(ext)
            if not lang:
                continue
            stats[lang]['files'] += 1
            try:
                content = fpath.read_text(errors='ignore')
                stats[lang]['lines'] += content.count('\n') + 1
            except Exception:
                pass
    # Sort by lines desc
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['lines'], reverse=True)
    return [{'language': k, 'files': v['files'], 'lines': v['lines']}
            for k, v in sorted_stats[:15]]


def readme_content(root):
    for name in ['README.md', 'readme.md', 'README.rst', 'README.txt', 'README']:
        p = Path(root) / name
        if p.exists():
            try:
                content = p.read_text(errors='ignore')
                return {'filename': name, 'content': content[:8000]}
            except Exception:
                pass
    return None


def package_info(root):
    """Extract project metadata from common config files."""
    info = {}
    # package.json
    pj = Path(root) / 'package.json'
    if pj.exists():
        try:
            data = json.loads(pj.read_text())
            info['package_json'] = {
                'name': data.get('name'),
                'version': data.get('version'),
                'description': data.get('description'),
                'license': data.get('license'),
                'dependencies': list(data.get('dependencies', {}).keys())[:20],
                'devDependencies': list(data.get('devDependencies', {}).keys())[:20],
                'scripts': data.get('scripts', {}),
            }
        except Exception:
            pass
    # pyproject.toml
    pp = Path(root) / 'pyproject.toml'
    if pp.exists():
        try:
            content = pp.read_text()
            info['pyproject_toml'] = content[:2000]
        except Exception:
            pass
    # Cargo.toml
    ct = Path(root) / 'Cargo.toml'
    if ct.exists():
        try:
            content = ct.read_text()
            info['cargo_toml'] = content[:2000]
        except Exception:
            pass
    # go.mod
    gm = Path(root) / 'go.mod'
    if gm.exists():
        try:
            content = gm.read_text()
            info['go_mod'] = content[:2000]
        except Exception:
            pass
    return info


def main():
    repo_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    repo_path = str(Path(repo_path).resolve())

    if not Path(repo_path).is_dir():
        print(json.dumps({'error': f'Directory not found: {repo_path}'}))
        sys.exit(1)

    repo_name = Path(repo_path).name

    result = {
        'repo_name': repo_name,
        'repo_path': repo_path,
        'git': git_info(repo_path),
        'file_tree': file_tree(repo_path),
        'language_stats': language_stats(repo_path),
        'readme': readme_content(repo_path),
        'package_info': package_info(repo_path),
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
