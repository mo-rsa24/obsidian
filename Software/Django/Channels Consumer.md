---
aliases: [Channels Consumer, Channels consumer, Django Channels consumer, WebSocket consumer, WebSocket consumers, websocket consumer, websocket consumers, AsyncWebsocketConsumer, WebsocketConsumer]
standard: vault-note v2
---

# Channels Consumer

Up: [[Django]]

Software, Django. A consumer is where a WebSocket lives in a Django app; consumers reach each other through the [[Channel Layer]], and the connection itself is a [[WebSocket]].

**A Channels consumer is a Django Channels class that holds one WebSocket connection from open to close: `connect` accepts it and joins groups, `receive` handles each message from the browser, and handler methods push messages back, the way a view handles one HTTP request.**

> [!warning]- Unfinished
> - The explanation is not written yet. This note holds only its card, under Where to learn this, and the next walk that teaches consumers writes the rest around it.

## Where to learn this

**Channels consumer**, the class that holds one WebSocket in Django Channels. Also: WebSocket consumer, AsyncWebsocketConsumer, WebsocketConsumer.

**Videos**

- Dennis Ivy, Django Channels & WebSockets Oversimplified, Consumers, 5:30 to 7:08: [watch](https://www.youtube.com/watch?v=cw8-KFVXpTE&t=330s). A consumer written on screen for a chat app, connect and receive, straight after the WebSocket connection is opened from the browser. Chapter-timed.
- Dennis Ivy, the same video, Routing configuration in ASGI, 7:40 to 8:49: [watch](https://www.youtube.com/watch?v=cw8-KFVXpTE&t=460s). The consumer routed from asgi.py's ProtocolTypeRouter, the wiring Attica's main/routing.py has. Chapter-timed.

**Our plans and chapters**

- [Channels websocket push](/home/molef/goal-setting/learning/projects/attica/event-creation/plans/02-rebuild-from-scratch/plans/23-channels-websocket-push.md), projects/attica/event-creation, rebuild plan 23. A Channels consumer over the Redis channel layer for Attica, the /ws proxy rule fixed and the 101 handshake watched in DevTools.
- [Async Django (ASGI/Channels)](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/03-operations-and-delivery/plans/03-async-django-channels.md), projects/tms-mobility. Django Channels standing up a persistent WebSocket connection with an async consumer.
- [Real-Time Dispatch Delivery](/home/molef/goal-setting/learning/projects/tms-mobility/system-design/plans/04-dispatch-integration-and-architecture/plans/03-realtime-dispatch-delivery.md), projects/tms-mobility. Consumers pushing dispatch updates to drivers over the channel layer.

> [!note]- How this was checked
> Every line under Where to learn this was opened before it was written, on 2026-10-27. No shelf book teaches Django Channels, so the card has no Textbooks group. The video's chapter list was read with cache-video-chapters.py; each plan's goal paragraph was read. Bare "consumer" is not an alias, because the learning tree also uses it for Kafka consumers (see [[Consumer Group]]).
