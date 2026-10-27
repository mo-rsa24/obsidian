---
aliases: [OpenStreetMap, Nominatim, geocoding, reverse geocoding, geocoder, map tiles]
standard: vault-note v2
---

# OpenStreetMap

Up: [[Software]]

Software, maps. OpenStreetMap is the one outside service Attica's event wizard calls from the browser: Nominatim turns the address typed in step 4 into a point on the map.

**OpenStreetMap is a free, community-built map of the world; its Nominatim service does geocoding (an address or place name to latitude and longitude) and reverse geocoding (a point back to an address), and its tile servers draw the map itself.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches geocoding writes the rest around it.

## Where to learn this

**OpenStreetMap**, the open world map and its geocoding service, Nominatim. Also: geocoding, reverse geocoding, map tiles.

**Videos**

- LizardTech, Getting Started with Nominatim: Geocoding & Reverse Geocoding, 0:00 to 1:12: [watch](https://www.youtube.com/watch?v=nTt-l6-QQCc&t=0s). Both directions, an address to a point and back, from OpenStreetMap data. Whole video.
- Try an API, OpenStreetMap, Geocoding data with the Nominatim OpenStreetMap API, 0:00 to 0:45: [watch](https://www.youtube.com/watch?v=29q5xkJ-YFE&t=0s). One Nominatim search request and the JSON it returns. Whole video.

**Our plans and chapters**

- [Location, Pricing, Amenities](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/01-tour-the-real-flow/plans/04-location-pricing-amenities.md), projects/attica/event-creation, tour plan 04. Step 4's address search watched as a GET to nominatim.openstreetmap.org in DevTools, the flow's one external dependency.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. No shelf book teaches geocoding or OpenStreetMap, so the card has no Textbooks group. Each video's chapter list was read with cache-video-chapters.py; the plan's step was read.
