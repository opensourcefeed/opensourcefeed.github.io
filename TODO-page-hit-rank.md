# Page Hit Rank: Enhancement TODO

Prioritized list of improvements for [/page-hit-rank/](page-hit-rank.md).
Items are ordered by impact relative to effort. Do them top to bottom.

Baseline (2026-11-04): 1,133 views across 140 OSes in 30 days (top entry: 36 views),
263 views across 24 desktops. The "previous" snapshot is ~12 hours older than "current".

---

## P0: Fix misleading data (quick wins)

- [x] **Compare trends against the previous 30-day window, not the last pipeline run.**
      `meta.previous_date` is currently ~12h before `current_date`, so ↑/↓ arrows are noise.
      Done in `assets/pageview/fetch4.py` (fetches current + preceding window per period).
- [x] **Show rank change as a number** (▲3 / ▼2 / NEW) instead of a bare arrow.
- [x] **Hide raw page-view counts.** Replace with a relative bar and/or a 0–100 index
      (`count ÷ leader × 100`). Applies to the rank page and to the distro/desktop layouts.
- [x] **Clean junk URLs in the pipeline**, not only in the template
      (e.g. `/desktop/games`, `/distribution/wordle-unlimited`,
      `/distribution/manjaro/<uuid>`, `/distribution/windows`).
- [x] **Merge hits from alias/redirect URLs** into their canonical page before ranking.

## P1: SEO foundations

- [x] **Dynamic, dated title**: "Most Popular Linux Distributions (November 2026) – Popularity Index";
      `fetch4.py` updates the month on each run.
- [x] **Data-driven summary** in the header (leader, top climber, base mix of the top 20,
      new entries). Kept to a few sentences instead of 300–600 words of filler.
- [x] **`ItemList` JSON-LD** for the current top 10 on each live page.
- [ ] ~~`Dataset` JSON-LD~~ skipped: there is no downloadable dataset to describe.
- [ ] ~~FAQ section with `FAQPage` schema~~ skipped: Google limits FAQ rich results to
      authoritative government/health sites, and the summary + methodology already answer these.
- [x] **Visible "Methodology" section** (done in P2).
- [x] **Separate URL for desktop environments**: `/page-hit-rank/desktop-environments/`
      (old `?type=desktop` links redirect). The 3-month view stays a `?period=3m` toggle,
      since a separate URL would mostly duplicate the 30-day page.
- [x] **Distro/desktop page rows** read "#8 in the Popularity Index (▲ 2)".
- [x] **Base-family pages**: `/distribution/{debian,ubuntu,arch,fedora,gentoo,slackware}-based/`
      and `/distribution/bsd/`, each with a short intro and its distros ranked by
      reader interest. Linked from the rank page, `distribution.md` and each distro's
      "Base distributions" row. Desktop pages already list their distros, so no
      per-desktop landing pages.

## P2: Premium visual redesign

- [x] **Top-3 podium** with logo, name, base, latest version and rank change.
- [x] **"Biggest movers" strip**: top 3 risers and top 3 fallers.
- [x] **Card/row layout with logos** replacing striped Bootstrap tables;
      relative-popularity bar per row; base and DE chips.
- [x] **Extra filters**: base family and desktop environment (shareable via `?base=` / `?de=`).
- [ ] **Use-case filter** (gaming / privacy / lightweight): needs a new `use_cases`
      front matter field on distribution pages first.
- [x] **Move the ad** below the podium or first table, not between tables and context.
- [x] **CSS variables** for all rank-page colors (`--rk-*` on `.rank-page`).
- [ ] **Dark-mode overrides**: add once the site itself gets a dark theme.
- [x] **Performance:** replace the four nested `site.pages` loops with a single lookup map.

- [x] **Same filters on [distribution.md](distribution.md)**: base and desktop filters
      combined with name search, "Most popular" sort, rank badge and base line on each card.

## P3: History and archives

- [x] **Store a monthly snapshot** (`_data/rank_history/YYYY-MM.yaml`, plus `YYYY.yaml` per year).
      `fetch4.py` keeps the last 12 complete months and every complete year since 2023;
      existing snapshots are frozen (`--rebuild-history` regenerates them).
- [x] **Sparklines / trend chart** for the top 10 over the last 6–12 months.
- [x] **Frozen monthly archive pages** (`/page-hit-rank/2026/10/`) linked from a
      "Previous months" list on the main page.
- [x] **Year-end page** ("Most Popular Linux Distros of 2026"), reviving the
      2021 "top 5 distributions" post format.

## P4: Composite popularity index (differentiator)

- [ ] **Pick external signals** and their weights (e.g. site hits 30%, GitHub stars/commit
      activity, subreddit subscribers, Google Trends, Flathub/AUR/Repology data).
- [ ] **Build the fetch + scoring job** that outputs the blended score into `rank.yaml`.
- [ ] **Document the methodology** on the page; show per-signal breakdown on hover/expand.
- [x] **Rename navbar item** "Page Hit Rank" → "Popularity Index" (keep the `/page-hit-rank/` URL).

## P5: Distribution and backlinks

- [ ] **Monthly "Top 10 distros this month" blog post** plus social posts.
- [ ] **Embeddable "Ranked #N on OpenSourceFeed" badge** for distro maintainers.
- [ ] **Outreach** to distro maintainers that rank or climb notably.
