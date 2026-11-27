# Koran 27 — notes (27 November 2026)

Competition: `news-image-20261127` — "Sum up 27 November's world news in
one image". $100 total, free entry, deadline 29 Nov 2026 07:00 WIB.
Judge: z-ai/glm-5.3-flash (vision), pairwise, no news feed — it judges by
what the image itself shows. Image must name the day it sums up.

## The six stories (all verified against live reporting, 27 Nov 2026)

### 1. LEAD — US: "The storm that stole Thanksgiving"
- A nor'easter battered the US East Coast on Thanksgiving Day; more than
  800,000 people without power (The Times, 27 Nov; peak 800k+; Virginia
  ~200k, Maryland ~177k), gusts to 70 mph (56 mph at LaGuardia).
- Macy's Thanksgiving Day Parade postponed for the first time in its
  100-year history, moved to Saturday 28 Nov, 8:30am (WSJ, The Times,
  Fox Weather). Balloons only fly below 23 mph sustained / 34 mph gusts.
- Sources: thetimes.com, wsj.com, foxweather.com, Newstalk ZB (27 Nov).
- Honesty note: the postponement was announced Wed 26 Nov (US) and the
  storm hit Thu 26 Nov (US); impacts ran through Fri 27 Nov and the story
  led 27 Nov editions worldwide (incl. Asia-Pacific morning editions dated
  27 Nov). The deck does not claim the storm started on Friday.

### 2. UKRAINE: "Zelenskyy warns of a new strike on the power grid"
- President Zelenskyy warns Russia could launch another major attack on
  the power grid and essential services (27 Nov "World in 90 seconds"
  briefing, Global Pulse).
- EU leaders remain split on financing Ukraine next year; a proposed
  €45 billion bloc-backed loan is on the table (same briefing; EU leaders
  also discussing the ~€1.6 trillion 2028–2034 budget).
- Sources: facebook.com/Global Pulse briefing 27 Nov; Times of India /
  Jagran school-assembly roundups 27 Nov.

### 3. NEW ZEALAND: "Final votes to decide a knife-edge parliament"
- Final election results due Friday 27 Nov; official count (incl. ~400,000
  special votes) expected to confirm whether the incumbent centre-right
  government holds its razor-slim majority — interim 67 of 131 seats
  (Reuters, WELLINGTON Nov 27; Newstalk ZB Morning Edition 27 Nov).
- Source: reuters.com via sumi.news; iheart.com News Fix 27 Nov 2026.

### 4. THAILAND: "Blast at Bangkok refinery injures nine"
- Explosion + fire at Bangchak's Phra Khanong refinery, Bangkok, ~2:45pm
  local; 9 injured, 3 critical (Erawan Medical Center); fire out in
  ~30 minutes; all production units shut; 120,000 bpd capacity; cause
  under investigation (AP, CNN, Reuters).
- Sources: cnn.com, reuters.com, AP via lapost.com / businessmirror.com.ph.
- Honesty note: the blast happened Thu 26 Nov ~14:45 Bangkok time
  (07:45 UTC) — i.e. 26 Nov in every timezone. It is included because it
  dominated 27 Nov morning coverage in Asia (lead story in 27 Nov
  roundups/briefings) and the deck does not date the blast itself; the
  page is dated 27 Nov. If the parent prefers strict 27-Nov-only events,
  swap this cell for the Cairo tanker fire (31 killed, listed in 27 Nov
  roundups) or the Pakistan–Saudi–Turkey meeting in Islamabad (27–28 Nov).

### 5. BLACK FRIDAY: "Deals deepen as shoppers hunt essentials"
- 27 Nov 2026 is Black Friday. Shoppers buying everyday essentials as
  well as gifts; Salesforce reporting larger November discounts than last
  year (27 Nov briefing). NZ: 1 in 3 retailers upping sales; Consumer NZ
  found half of tracked products same price or cheaper at other times
  (Newstalk ZB 27 Nov).
- Sources: Global Pulse briefing 27 Nov; iheart.com News Fix 27 Nov.

### 6. SPORT strip
- Pittsburgh Steelers released QB Aaron Rodgers after ten starts; Mason
  Rudolph to start vs Denver (27 Nov briefing).
- Jannik Sinner out of Australian Open 2027 due to knee injury
  (27 Nov roundups).
- Sources: Global Pulse briefing 27 Nov; thedailyjagran.com 27 Nov.

## Build & test

- `build.py` draws `entry.png` (1024×1024, PIL, Liberation Serif /
  DejaVu Sans, flat editorial illustration, no external assets).
- `main.py` copies `entry.png` to `/output/entry.png`; no network, no
  randomness.
- Test (run from the build dir):
  - `python3 build.py` → entry.png 120,041 bytes, 1024×1024.
  - `python3 main.py` twice → /output/entry.png sha256 identical both
    runs, 120,041 bytes, under the 1 MiB cap.
- Viewed the final PNG myself: masthead, date, all six stories, sport
  strip and sources footer fully legible; two fixes applied after the
  first render (fact line no longer runs under the storm panel; panel
  caption no longer clipped).

## Session / recording note

- The `makefun` CLI was NOT available in this build session (no `makefun`
  binary on PATH; ~/.makefun holds only logs/credentials), so no
  `makefun record` session could be started here. The parent agent owns
  submit-time transcripts/seal — flag before submitting.
- No push to GitHub, no submit — awaiting fadli's verdict + explicit
  submit confirmation.
