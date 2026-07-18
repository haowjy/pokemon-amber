# Webnovel / Inkstone

- Published list template: `https://inkstone.webnovel.com/novels/view/{novel_id}?targetTab=published`
- Discover edit URLs from every pagination page.
- Title textbox accessible name: `Title Here`; use `canonical_title`. Do not add another chapter prefix.
- Editor iframe IDs are dynamic. Select the observed `iframe[title^="Rich Text Area"]`, then its body.
- Existing chapter submit: unique `update` button; require `Chapter saved!`.
- New chapter: click `CREATE CHAPTER`, fill title and body, click `Publish`, review the `confirm publish` dialog, then click exact `confirm`.
- Compare final order and titles against the local export rather than trusting existing numbering.
