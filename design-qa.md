# Slate Horizon implementation QA

Source visual truth: `/Users/jiahui/Documents/Playground/yangon-heroes/glass-concepts/02-slate-horizon.png` (1122 × 1402).
Implementation: `http://127.0.0.1:4173/?design=slate`.
Evidence directory: `/Users/jiahui/Documents/Playground/yangon-heroes/glass-concepts/`.

## Capture and comparison

- Desktop CSS viewport 1122 × 1402, devicePixelRatio 1.75. In-app capture returns the visible window region as 1114 × 1032 pixels, excluding scrollbar and clipping the lower portion. Compare the corresponding top portion of the source at the same scale; do not treat clipping as layout failure.
- `slate-desktop-final.png`: page at scrollY 0; source and implementation opened together in the same comparison tool input. Header, first hero, dock and start of second hero compared.
- `slate-content-final.png`: focused second-section evidence for readable text, image crop and action.
- `slate-plans-final.png`: expanded plan content and glass cards (before final equal-height text alignment).
- `slate-mobile-final.png`: CSS viewport 390 × 844, scrollY 0. Mobile is a responsive interpretation; no mobile source was supplied.
- Full-page capture is heavily downscaled by this browser and was not used to judge fine detail.

## Comparison history / resolved findings

1. P2: navigation too wide and second hero text too low. Reduced desktop header width from 85% to 74%, moved second-section text from 22% to 12%. Evidence: initial `slate-desktop.png` versus final desktop and focused content captures.
2. P2: photo crop hid too much of the original city activity. Repositioned the first image below the header with a soft upper mask. Preserved approved original assets instead of regenerating the spokesperson.
3. P2: fixed mobile pause button covered primary dock controls. Moved it above hero copy, made it scroll with the document; final mobile capture confirms clear headline and control separation.
4. P2: scene boundary was abrupt. Added top/bottom image opacity masks over a common slate background. Final desktop capture shows gradual blending into scene 02.

## Required fidelity surfaces

- Typography: DM Sans with Noto Sans Myanmar. Bold white English heading, Burmese secondary heading, legible body text. Burmese wraps more than in the image mock because real font shaping is retained. No text overflow detected in any desktop hero.
- Spacing: compact glass nav, left first-hero copy, bottom floating action dock, right second-hero copy. Responsive mobile separates copy and scene rather than shrinking the desktop interface.
- Color: unified navy/slate/ice-blue tokens. Glass translucency, pale primary buttons, outlined secondary button, blue-grey inter-scene fade retained. Slightly darker overlays intentionally protect readability when future video luminance varies.
- Assets: all 10 approved v4 source images preserved as 1672 px WebP images. Mock repositioned some background subjects; original identity and scene fidelity take priority over reproducing regenerated microdetails. Baked-in social cards remain in original image. No replacement drawn icons.
- Copy: 10 scenes and 3 provisional plans, Burmese/English only. Checked 0 Chinese characters in rendered HTML, one h1, ten video slots. No fabricated prices, phone number or performance metrics. Concept-name label removed from mock because it is not company branding.

## Interactions

- Explore services, Plans and back-to-home anchors tested in the browser; all hash targets resolve.
- Social Management selection appears in contact section.
- Copy Facebook Page name succeeds and shows feedback.
- Pause motion toggles its accessible pressed state and page state.
- No horizontal overflow at desktop 1122 and mobile 390 CSS px.
- All ten images report naturalWidth 1672; no browser console errors observed.

## Follow-up / limitations

- Actual MP4 playback, autoplay rejection, decoding, loop seams and mobile video crops must be verified when the first real video arrives. Current media map intentionally empty.
- Page URL is not supplied; contact flow copies the confirmed Page name, not a guessed URL.
- Native Burmese proofreading before public launch is recommended; copy is provisional.
- The Wordmark is retained as live type without the decorative arrow. Remaining crop differences from the mock are accepted to retain approved images and prepare video composition.

Implementation checklist: responsive styling, image/video slots, navigation, plan selection, contact copy, motion preference handling complete for the current image-backed stage.

final result: passed
