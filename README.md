# Nikita Obraztsov — academic website

Bilingual Hugo website: https://nikitaobraztsov.com/.

## Working on either Mac

1. In GitHub Desktop, Fetch origin and Pull origin before editing. Do not copy an old checkout over the current repository.
2. Open the repository root as the Obsidian vault. Disable Wikilinks and automatic link updates (Hugo URLs differ from filesystem paths).
3. In Terminal, from the repository root, run:

   ```bash
   hugo server -D --port 1313 --disableFastRender
   ```

   Preview English at http://localhost:1313/ and Russian at http://localhost:1313/ru/. Stop with Ctrl+C.
4. Check the production build and internal links: `python3 scripts/check_links.py`.
5. Review the diff, commit and push in GitHub Desktop. [GitHub Actions](https://github.com/nikobraztsov/nikobraztsov.github.io/actions) builds with Hugo Extended 0.162.1 and validates internal links before deployment.

## Content

| English | Russian |
|---|---|
| `content/news/` | `content-ru/news/` |
| `content/media/` | `content-ru/smi/` |
| `content/texts/` | `content-ru/texts/` |
| `content/about/index.md` | `content-ru/about/index.md` |
| `content/research/index.md` | `content-ru/research/index.md` |
| `content/publications/index.md` | `content-ru/publications/index.md` |
| `content/talks/index.md` | `content-ru/talks/index.md` |

New Markdown filenames end in `-en.md` or `-ru.md`; use a shared `slug` and `translationKey` for paired posts. Example:

```yaml
---
title: "Example"
date: 2026-11-26
slug: "example"
translationKey: "example"
description: "Short description."
tags: ["research"]
draft: false
---
```

Use first person in personal writing, neutral bibliographic entries for publications and event records. Preserve existing URLs; do not rename old pages without checking aliases and links. Place PDFs/images in `static/` and link to `/docs/file.pdf`, `/images/file.jpg`, or `/cv.pdf` (never `/static/`). Update `static/cv.pdf` and `static/cv-ru.pdf` under their existing filenames. Do not commit generated `public/` or local workspace files. Back up files before destructive edits.

## Credits and license

Based on [Pascal Michaillat's academic Hugo template](https://github.com/pmichaillat/hugo-website) and [PaperMod](https://github.com/adityatelange/hugo-PaperMod). See the [original template documentation](https://pascalmichaillat.org/b/) and [MIT license](LICENSE.md). Author content and third-party media may have separate rights.
