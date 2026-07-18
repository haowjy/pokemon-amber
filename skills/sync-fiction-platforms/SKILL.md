---
name: sync-fiction-platforms
description: >-
  Use when synchronizing fiction chapters from a project's canonical source to
  Royal Road, FanFiction.net, Webnovel, AO3, or another browser-based publishing
  dashboard. Normalizes chapter content, inventories remote chapters, updates
  published prose, and publishes missing chapters without assuming a source
  format, repository layout, or story.
---

# Sync Fiction Platforms

Use the browser surface the user selected. Load that browser's control skill before acting.

## Optimize model and context

- When execution-model selection is available, prefer **GPT-5.6 Terra, medium effort** for a normal sync.
- Use Sol only for unfamiliar layouts, ambiguous state, failed saves, or recovery.
- Never emit entire chapter-editor snapshots. Inspect the smallest relevant state: title, editor presence, buttons, success message, and chapter list.
- Confirm a platform template once, then reuse its verified selectors. Still obtain fresh page state after every navigation.

## Prepare canonical content

Discover how the project represents and renders canonical chapters. Prefer its existing export or build path over a bundled adapter. Do not assume Markdown, frontmatter, filenames, directory layout, numbering style, or repository storage.

Normalize only the requested publication scope into records containing:

- stable chapter identity and ordering
- canonical title
- rich HTML when available
- plain-text fallback
- source location or provenance for verification

Read [references/content-sources.md](references/content-sources.md) when the project does not already provide publishable HTML and text.

Look for project-local publishing metadata using the project's own conventions. If none exists, discover story IDs from authenticated dashboards and keep them as session state. Do not invent a configuration location or persist identifiers unless the user asks.

Adapt titles to each platform's numbering behavior. Never add a prefix merely because another platform uses one.

## Run the sync

1. Inventory remote chapter identities and titles from list pages. Do not open every editor during inventory.
2. Compare the inventory to the normalized requested chapter set. Do not infer inclusion of interludes, side stories, drafts, hidden chapters, or other special entries.
3. Obtain one explicit authorization before the first live save/publish. Explain that a newly published chapter can notify readers.
4. Update one chapter on each platform and verify the success marker.
5. Bulk-update the remaining chapters with the verified template. Stop on CAPTCHA, authentication loss, selector ambiguity, or a missing success marker.
6. Reopen each platform's chapter list. Success means every requested chapter is present once, in order, with the expected title, and every save produced its platform success marker.
7. Report platform-by-platform results and any temporary staging-document side effects.

Load only the resources for requested platforms:

- [references/royal-road.md](references/royal-road.md)
- [references/fanfiction-net.md](references/fanfiction-net.md)
- [references/webnovel.md](references/webnovel.md)
- [references/ao3.md](references/ao3.md)

## Safety and failure boundaries

- Publish only the chapter scope the user authorized.
- Never delete, reorder, unpublish, or overwrite a different story.
- Do not bypass CAPTCHA or platform security restrictions.
- Do not automate AO3 when the Browser runtime blocks `archiveofourown.org`; provide exported HTML for manual paste instead.
- Treat document-manager documents as staging artifacts, not canon. The published chapter and repository prose are authoritative.
- Do not commit repository changes unless the user asks.
