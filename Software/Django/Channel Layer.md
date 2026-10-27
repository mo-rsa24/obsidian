---
aliases: [Channel Layer, channel layer, channel layers, channel_layer, Channels channel layer]
standard: vault-note v2
---

# Channel Layer

Up: [[Django]]

Software, Django. The channel layer is how one [[Channels Consumer]] reaches another, and in Attica it is [[Redis]] db 0: a small [[Publish-Subscribe]] system inside Django Channels.

**A channel layer is Django Channels' message bus between processes: each consumer has a channel name, consumers join named groups, and `group_send` delivers a message to every consumer in a group, wherever it runs, through a backend such as Redis.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches the channel layer writes the rest around it.

## Where to learn this

**Channel layer**, the message bus that lets Channels consumers reach each other. Also: channel_layer.

**Videos**

- Dennis Ivy, Django Channels & WebSockets Oversimplified, Channel Layers Explained, 11:50 to 16:35: [watch](https://www.youtube.com/watch?v=cw8-KFVXpTE&t=710s). Why one consumer cannot reach another without a layer, then groups and group_send with Redis behind them, for a chat room. Chapter-timed.
- Dennis Ivy, the same video, Sending Messages, 8:49 to 11:50: [watch](https://www.youtube.com/watch?v=cw8-KFVXpTE&t=529s). A message sent back through the consumer, the step the channel layer then fans out to everyone. Chapter-timed.

**Our plans and chapters**

- [Channels websocket push](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/23-channels-websocket-push.md), projects/attica/event-creation, rebuild plan 23. Attica's push rebuilt over the Redis channel layer, with two tabs updating live to show the fan-out.
- [Real-Time Dispatch Delivery](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/04-dispatch-integration-and-architecture/plans/03-realtime-dispatch-delivery.md), projects/tms-mobility. Dispatch updates fanned out to drivers through the channel layer's groups.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. No shelf book teaches the Channels channel layer (a page-text search found "channel" and "layer" only in convolutional networks and the link layer), so the card has no Textbooks group. The video's chapter list was read with cache-video-chapters.py; each plan's goal paragraph was read.
