# Current video delivery

All 10 heroes now have H3 video backgrounds. City keeps the approved 8-second dual-reference pilot; scenes 02–10 are exactly 5 seconds, 1344 × 768, 24 fps, silent H.264 MP4. Each generation uses the approved scene and original face reference separately.

Preview the website at http://127.0.0.1:4173/?design=slate and the individual clips at http://127.0.0.1:4173/video-review.html .

Sources are mapped in `dist/media.js`. All prompts, native requests, task IDs, original video outputs, contact sheets and final clips are retained in `../videos/h3-series-5s/`. See `DELIVERY.md` and `manifest.json` there.

The website retains image posters, visibility-based loading/playback, background pause, reduced-motion support, manual pause and error fallback. Videos contain one completed action with subtle environmental movement. They are not guaranteed seamless loops. Native multi-reference mode guides identity and scene composition but does not enforce a pixel-exact first frame.
