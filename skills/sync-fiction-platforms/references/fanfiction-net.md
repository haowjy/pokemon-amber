# FanFiction.net

- Story content template: `https://www.fanfiction.net/story/story_edit_content.php?storyid={story_id}`
- Document manager: `https://www.fanfiction.net/docs/docs.php`
- A reusable staging document is sufficient. Use a profile's staging-document ID or select one from the document manager; verify that its editor loads before use.
- Staging editor body: `frameLocator("#bio_ifr").locator("body")`; submit the unique `Save` button.
- For each chapter, update the staging document, save it, and immediately replace the intended published chapter before reusing it.
- Open `Replace/Update Chapter` and use these accessible controls:
  - chapter selector: `Please select the chapter to replace/update.`
  - document selector: `Please select the document to use as the content replacement.`
  - submit: `Replace Chapter Content with Document`
- Require `Content Replaced` after every replacement.
- The title editor is the row's pencil image with title `Edit Chapter Title`. FFN limits and normalizes titles; only correct material mismatches.
- Document labels may be stale because documents are temporary staging. Report this; do not assume label-to-chapter correspondence.
