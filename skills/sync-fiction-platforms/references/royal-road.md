# Royal Road

- Chapter list template: `https://www.royalroad.com/author-dashboard/chapters/list/{story_id}`
- Discover edit URLs from the chapter list; do not retain chapter-edit IDs as durable configuration.
- Title field: `#Title`; use `canonical_title`.
- TinyMCE body: `frameLocator("#contentEditor_ifr").locator("body")`.
- Replace content using rich clipboard HTML with the manifest's plain text as fallback.
- Submit the unique `Save Changes` button.
- Require `Your chapter has been successfully edited.` after every save.
- Verify final count, order, and titles from the chapter list.
