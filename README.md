# SJ Wiki

Personal notes on **Mathematics**, **Computer Science**, **Physics**, and **Chemistry**, built with [Docusaurus](https://docusaurus.io/).

Live site: `https://justinbrianhwang.github.io/SJ-wiki/` *(after first deploy)*

## Local development

```bash
npm install      # install dependencies (first time only)
npm start        # start dev server at http://localhost:3000
npm run build    # build static site into ./build
npm run serve    # preview the production build locally
```

## Adding a new note

1. Find or create a folder under `docs/math/<topic>/` or `docs/cs/<topic>/`.
2. Create a new `.md` (or `.mdx`) file. Front matter is optional:
   ```md
   ---
   title: My Topic
   sidebar_position: 3
   ---

   # My Topic

   Content goes here.
   ```
3. Math expressions use LaTeX syntax: `$inline$` or `$$display$$`.
4. The sidebar auto-updates from the folder structure — no manual config needed.

## Adding a new top-level category

1. Create the folder, e.g. `docs/math/topology/`.
2. Add a `_category_.json`:
   ```json
   {
     "label": "Topology",
     "position": 6,
     "link": { "type": "doc", "id": "math/topology/intro" }
   }
   ```
3. Add `intro.md` inside that folder.

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the site and publishes to GitHub Pages.

One-time setup: in the GitHub repo, go to **Settings → Pages** and set the source to **GitHub Actions**.

## Project structure

```
docs/
├── math/
│   ├── linear-algebra/
│   ├── engineering-math/
│   ├── statistics/
│   ├── probability/
│   └── discrete/
└── cs/
    ├── algorithms/
    ├── data-structures/
    ├── systems/
    └── theory/
```
