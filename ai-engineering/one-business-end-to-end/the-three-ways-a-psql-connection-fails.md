---
scope: ai-engineering/one-business-end-to-end
goal: /home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/MASTER_PLAN.md
produced: 2026-09-15
---

# The three ways a psql connection fails

An interactive walk built from the textbook's own worked failures: [Three ways psql fails](https://claude.ai/artifact/9pUEc5xonsigESLoAU3FH6).

The connection string routes through a chain: client, Unix socket, server process, database, table.
Each failure stops at a different point in that chain, and the first line psql prints says which
point it was.

**Fail 1, wrong database name.** The server answered and the socket is live; the request reaches the
database stage and stops there, because `coffee_shp` is one letter short of `coffee_shop`. First
line: `psql: error: ... FATAL: database "coffee_shp" does not exist`.

**Fail 2, nothing listening.** The request never gets past the server stage: a stopped server, a
wrong port, or a container not yet up. First line: `psql: error: ... Connection refused`.

**Fail 3, connected, wrong query.** The chain completes all the way to the table stage; the SQL is
wrong (`sale` not `sales`), not the connection. First line starts `ERROR:` rather than `psql: error:`.

The prefix alone tells the two families apart: `psql: error:` means never connected (fails 1 and 2);
`ERROR:` means connected, the SQL is wrong (fail 3). A retry that only catches crashes catches the
first two and misses the third.

Source: [00-standing-the-shop-up.md](/home/molef/goal-setting/learning/ai-engineering/one-business-end-to-end/textbook/00-standing-the-shop-up.md), section 0.3.
