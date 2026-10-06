# Walks write the vault (PC walk): illustrated map

The drawn pictures this walk uses to test what a general note's pictures look like. 1 prompt · 1 rendered · 0 waiting.

## Table of contents

- [Abstraction chain](#abstraction-chain)
- [Art direction](#art-direction)
- [Reference images](#reference-images)
- [Meaning palette](#meaning-palette)
- [Reading axes](#reading-axes)
- [Devices in play](#devices-in-play)
- [Subject lane](#subject-lane)
- [Process lane](#process-lane)

## Abstraction chain

Navigation: 📋 [TOC](#table-of-contents) | [Art direction](#art-direction) ➡️

1. [Walks write the vault (PC walk)](diagram-prompts.md): subject "One process holds port 8000"

## Art direction

Navigation: ⬅️ [Abstraction chain](#abstraction-chain) | 📋 [TOC](#table-of-contents) | [Reference images](#reference-images) ➡️

**Empty**, chosen by the user on 2026-10-01 from a shortlist of Empty, Glossy, Cartoon and Paper. The answer is kept for every drawn picture in a general note, since the brief asks for one look across the vault. Under Empty the finish is held constant by the finish reference `render-diagrams` attaches, and layout and palette are left to the renderer.

**Zoom depth: level 0 only**, chosen by the user on 2026-10-01. One picture shows the whole mechanism: the process, its four descriptors, what each points at, the port and the client. No component opens into a level 1. This matches the walk's decision that a thing gets two drawn pictures, the form and the mechanism, with a longer set on demand.

**Lane: subject**, chosen by the user on 2026-10-01. The picture shows what one `lsof` row describes at one instant, with no time in it.

## Reference images

Navigation: ⬅️ [Art direction](#art-direction) | 📋 [TOC](#table-of-contents) | [Meaning palette](#meaning-palette) ➡️

Attach each file with `-i` alongside every prompt that draws the thing it shows.

| File | What it is | Source and licence |
|---|---|---|
| `diagrams/refs/python.png` | the Python logo, used only on a process that is the Python interpreter | simple-icons 16.32.0 on jsDelivr (`https://cdn.jsdelivr.net/npm/simple-icons@16.32.0/icons/python.svg`), CC0-1.0, filled with the brand colour simple-icons records |

## Meaning palette

Navigation: ⬅️ [Reference images](#reference-images) | 📋 [TOC](#table-of-contents) | [Reading axes](#reading-axes) ➡️

Two colours carry meaning, and each keeps that meaning alone.

- Orange: a descriptor open for writing only (`w` in the FD column).
- Green: a descriptor open for reading and writing (`u` in the FD column).

No descriptor in the run is open for reading only, so no colour is assigned to `r`.

## Reading axes

Navigation: ⬅️ [Meaning palette](#meaning-palette) | 📋 [TOC](#table-of-contents) | [Devices in play](#devices-in-play) ➡️

Left to right: the process, then its descriptors, then what each descriptor points at. The right edge is the network, where the client arrives. The vertical axis carries the descriptor number, 0 at the top and 3 at the bottom.

## Devices in play

Navigation: ⬅️ [Reading axes](#reading-axes) | 📋 [TOC](#table-of-contents) | [Subject lane](#subject-lane) ➡️

Flow colour coding with an in-image legend. Callout chips, one per part, each saying in six words or fewer what that part is for, so the picture explains the row as well as showing it. One truth anchor: the `lsof` row itself, drawn small at the bottom edge. No sequencing devices, because this is a subject picture.

## Subject lane

Navigation: ⬅️ [Devices in play](#devices-in-play) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

The mechanism behind one row of `lsof -i :8000`, taken from a run on 2026-10-01 on the PC (WSL). The captured text is in [the output of that run](runs/lsof-output.txt) and [its descriptor table](runs/lsof-descriptors.txt).

### Prompt 1 (Subject): One process holds port 8000

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents) | [Process lane](#process-lane) ➡️

[observed] 🖼️ rendered 2026-10-01: `diagrams/lsof-01-one-process-holds-the-port.png`
Save as: `diagrams/lsof-01-one-process-holds-the-port.png`

Visual thesis: a port is held by one descriptor of one process, a row of `lsof` is a description of that one line, and every part of the row names something with a job.

```text
Style: no named house style is imposed, but the result is a clean, welcoming UI-grade picture and never a wireframe. Every component gets an icon, an emoji or a small illustration of what it actually is; a real product carries its official logo only where the component is that product; a physical thing (a RAM stick, a building, a server rack, a phone) is drawn as the real object, not a labelled box. Cards and panels are rounded, with a thin coloured border, a soft drop shadow and a lightly tinted background that tells groups apart; grey is kept for secondary text, dividers and things that are off or inactive. Light background, generous spacing, a clear type hierarchy. Any colour the prompt names a meaning for keeps that meaning alone. Beyond that, let the composition and visual treatment that best communicate this subject emerge from the context below, rather than from an imposed convention.

Scene: a landscape 16:9 teaching diagram of what one running program has open on a Linux machine, read left to right. On the left, one process. In the middle, its four numbered file descriptors stacked top to bottom, 0 at the top and 3 at the bottom. On the right, the three things those descriptors point at. At the far right edge of the canvas, the network side of the machine, with a door for port 8000 and a client arriving from outside. Along the bottom edge, a small monospace strip showing the single line of terminal output this picture explains. The process is the focal point and the descriptor numbered 3 and its line to the socket are the most prominent connection. Every fact in this picture was observed in a real run; nothing is planned or inferred, so nothing is drawn dashed.

Cast:
- The process: one running Python program, drawn as a rounded card with a small running-program illustration. The official Python logo may mark it, because the process is the Python interpreter. Three facts sit on the card: its name, its process number, and the user who owns it.
- The four file descriptors: four small numbered slots attached to the right side of the process card, like numbered sockets on a power strip. Each is a handle the process holds on something it has open.
- The null device: a small drain or empty bin illustration, standing for the special file that discards everything written to it.
- The log file: one ordinary document or file icon. There is only one log file, and two descriptors point at the same one.
- The network socket: a plug-shaped or endpoint illustration, larger than the file icons. It carries its kernel number, its protocol and its state.
- Port 8000: a numbered door or gate in the machine's network edge, at the far right. The socket sits directly behind this door.
- The client: a small terminal window outside the machine, to the right of the door, making a request.

Flows:
- Descriptor 0 to the null device: a green line, meaning open for reading and writing.
- Descriptor 1 to the log file: an orange line, meaning open for writing only.
- Descriptor 2 to the same log file: an orange line, meaning open for writing only. The two orange lines end on one file icon.
- Descriptor 3 to the network socket: a green line, meaning open for reading and writing. This is the thickest line in the picture.
- The socket to the port 8000 door: joined directly, the socket is what is listening behind the door.
- The client to the port 8000 door: one arrow arriving from outside the machine and ending at the door. It does not touch the process.
- A small legend inside the image: orange means "write only", green means "read and write".
- Lines do not cross.

Callout chips: six short explanatory chips, each a small rounded tag sitting beside the part it explains, joined to it by a thin dotted leader, never on top of an arrow. Each chip says what that part is for.
- Beside the process number on the process card.
- Beside the stack of four descriptors.
- Beside the null device.
- Beside the network socket.
- Beside the "TCP" label on the socket.
- Beside the port 8000 door.

Text in the image, exactly as quoted:
- Title: "One process holds port 8000"
- On the process card: "python3", "PID 232663", "user molef"
- On the descriptors: "fd 0", "fd 1", "fd 2", "fd 3"
- On the targets: "/dev/null", "server.log", "socket 7743610"
- On the socket: "TCP", "LISTEN"
- On the door: "*:8000"
- On the client: "curl localhost:8000"
- Legend: "write only", "read and write"
- Chip beside the process number: "the kernel's number for this process"
- Chip beside the descriptors: "numbered handles on open things"
- Chip beside the null device: "discards whatever is written"
- Chip beside the socket: "one end of a network conversation"
- Chip beside "TCP": "bytes arrive in order, or fail"
- Chip beside the door: "which program gets the traffic"
- Bottom strip, in monospace, one line: "python3 232663 molef 3u IPv4 7743610 0t0 TCP *:8000 (LISTEN)"

Exclusions: no second process, no fifth descriptor, no second log file, no database, no browser, no cloud, no logos other than the Python logo on the process, no colour for a read-only descriptor because none exists in this run, no step numbers or ordering badges, no dashed outlines. No duplicated components, no orphan arrows, no arrow terminating in whitespace, no color used without a legend entry, no decorative circuitry or filigree, no invented or misapplied brand logos, no paragraphs of text, no illegible pseudo-code, no crossing arrows where routing could avoid it, no untitled containers, no icon without a label, no perspective distortion applied to arrows, no visual metaphor that contradicts the system's actual semantics, no watermark, no geometric pictogram, circuit symbol, or bare connector line standing in for a real-world physical object the prompt names.
```

Faithfulness note: exactly one process and exactly four descriptors numbered 0 to 3; fd 3 is the only line reaching the socket, and the socket carries "socket 7743610", "TCP" and "LISTEN" and sits behind the door labelled "*:8000"; fd 1 and fd 2 are orange and both end on one "server.log"; fd 0 and fd 3 are green; the client's arrow ends at the door and never at the process; the process card reads "python3", "PID 232663", "user molef"; all six chips are present with their exact words, each joined to its own part by a dotted leader and none lying on an arrow; the bottom strip matches the captured row character for character.

## Process lane

Navigation: ⬅️ [Subject lane](#subject-lane) | 📋 [TOC](#table-of-contents)

Not authored. The mechanism picture for this thing is a subject picture by the choice recorded under [Art direction](#art-direction). The steps (start the server, bind, listen, a second server fails, `lsof` names the holder, `kill` frees the port) are carried by the lesson's "try it yourself" section and its output pictures.
