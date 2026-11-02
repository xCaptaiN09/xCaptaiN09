# One CRT monitor

The profile introduction uses one shared GitHub code-block surface. Its name, animated role line, live counters, seven destination links, setup cells and motto are all inside that one frame. The SVG content is transparent and has no separate outer screens, windows, title bars or rounded cards. Only the small setup cells have outlines. Metrics, statistics and the snake remain below the monitor.

The frame background follows GitHub's theme. The SVG lettering adapts to light and dark themes. The local preview uses GitHub-like spacing; the final GitHub page can differ slightly in spacing and theme colors.

The standalone footer screen and original artwork section are removed. The motto now lives inside the main monitor. Existing original bitmap files in the repository are not deleted by this update.

## Sources

| Content | Source | Updates |
| --- | --- | --- |
| Dot-matrix name, terminal commands, setup and motto | Assets/profile/monitor-*.svg | python3 scripts/build_crt_art.py |
| Role typing | Original readme-typing-svg service, with the same five phrases | External SVG animation |
| Views | Original Komarev username | Image request / service cache |
| Followers and stars | Original Shields username | Image request / service cache |
| Metrics and 3D calendar | github-metrics.svg | Original metrics.yml |
| Top languages | top-langs.svg | Original stats.yml |
| Streak | Original external service URL | Image request / service cache |
| Snake | Original output branch SVG | Original snake.yml |

Each command link is a separate HTML anchor around its SVG label. The counters remain separate live image requests, not fixed numbers in an illustration. No new workflow or secret is needed. All original destination URLs and the metrics/stats/snake content are preserved.

## Editing and preview

Run `python3 scripts/build_crt_art.py` to regenerate the eighteen transparent SVG assets using Python's standard library. Their backgrounds must remain transparent so GitHub's single parent frame supplies the continuous screen surface. The source contains desktop and mobile versions; mobile links are narrower and the setup uses two columns.

Run `python3 scripts/preview_profile.py` to open a localhost-only preview. Refresh after edits and press Ctrl+C to stop it. The external typing, counters, streak and snake need internet access. Generated statistics come from the local checkout. Reduced-motion settings disable the local cursor; the external typing service controls its own animation.

The supplied PNG is a static composition of the actual assets, a held typing phrase and fetched counter badges. It is a layout preview, not a browser screenshot. Counter numbers in this preview are snapshots; the README uses the live provider URLs.
