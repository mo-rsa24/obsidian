---
aliases: [lsof, list open files]
sources:
  - "man lsof, lsof revision 4.95.0, Ubuntu 24.04.2 on the PC (WSL), read 2026-10-01"
produced: 2026-10-03
---

<!-- Example of the subject-note shape, drafted by the PC walk on 2026-10-03. In the vault this note
would sit at Information Technology/Operating Systems/Linux.md, its pictures in assets/ as .webp,
and the links into the learning tree would be absolute paths. Here the pictures point back into
this walk's folder so they display. -->

# Linux

> [!question] Test yourself: quiz not built yet
> Covers [[#lsof]]. The link fills in once the quiz page is published.

> [!warning] Unfinished
> - 2 pictures are waiting: the kernel between the hardware and the processes, and the form of `lsof -i`.
> - No project has applied `lsof` yet. Only the writer's own sandbox runs exist.

Stated, not checked: 4 claims (Linux, the kernel, `0t` in SIZE/OFF, NODE for a socket), and 3 more under [[#Other ways]].

## Contents

- [[#What Linux is]]
  - [[#^def-linux|Linux]] ^nav-linux
  - [[#^def-kernel|Kernel]] ^nav-kernel
  - [[#^def-process|Process]] ^nav-process
- [[#Everything is opened the same way]]
  - [[#^def-fd|File descriptor]] ^nav-fd
- [[#lsof]]
  - [[#When to reach for it]]
  - [[#The form]]
  - [[#Try it yourself]]
  - [[#Reading the output]]
  - [[#A second example: a client is connected]]
  - [[#How it works]]
  - [[#Other ways]]
  - [[#Taught in, applied in]]

## What Linux is

↑ [[#Contents]]

**Linux[[#^nav-linux|:]]** an operating system: the program that runs every other program and shares the one machine between them. ^def-linux
- backing: stated

**Kernel[[#^nav-kernel|:]]** the core of Linux. It owns the memory, the disks and the network, and hands each of them out to programs that ask. ^def-kernel
- differs from: the programs you run, which never touch the hardware themselves and ask the kernel for everything
- backing: stated

**Process[[#^nav-process|:]]** one running copy of a program, with its own number, the PID. ^def-process
- differs from: a program, which is a file on disk. Starting the same program three times makes three processes.
- see it: `ps -p <PID>`
- in a run: the same server started three times on 2026-10-01 got PIDs 228372, 230394 and 232663
- backing: shown

> 🖼️ **Picture on its way:** the kernel between the hardware and the processes.

## Everything is opened the same way

↑ [[#Contents]]

Linux gives a process a small numbered handle for everything it opens. A file on disk, a device, a pipe between two programs and a [[Intro To Networking#Network|network]] connection all get the same kind of handle, and are read, written and closed the same way. This is why a tool that lists open files can also list network connections.

**File descriptor[[#^nav-fd|:]]** the numbered handle a process holds on one open thing. 0, 1 and 2 are taken at start for input, output and errors. ^def-fd
- in a run: one Python web server held four, read on 2026-10-01 with `lsof -a -p <PID> -d 0-3`
  - fd 0 on `/dev/null`, a device (`CHR`)
  - fd 1 and fd 2 on `server.log`, a regular file (`REG`)
  - fd 3 on a network socket (`IPv4`)
- backing: shown

## lsof

↑ [[#Contents]]

**lsof** lists the files a program has open, so it shows which program holds a port.

### When to reach for it

↑ [[#lsof]]

A server will not start because its port is taken, and the error does not say by what. `lsof` names the program, its PID and its owner, so you can decide whether to stop it.

### The form

↑ [[#lsof]]

```text
lsof -i :<port>                   every connection on that port
lsof -i :<port> -sTCP:LISTEN      only the program waiting for connections on it
lsof -t -i :<port> -sTCP:LISTEN   only its PID, ready to hand to kill
```

> 🖼️ **Picture on its way:** the form, with `-i`, `:<port>`, `-sTCP:LISTEN` and `-t` each named.

### Try it yourself

↑ [[#lsof]]

All of this runs in an empty folder. Nothing here touches a real project.

**1. Check you have it.**

```bash
lsof -v 2>&1 | grep revision
```

You should see a line with `revision: 4.95.0` or similar. Ran 2026-10-01, PC (WSL, Ubuntu 24.04.2).

**2. If it is missing.** On Ubuntu, `sudo apt install lsof`. Not run here, since the writer never installs onto the machine. Backing: stated.

**3. Make something to look at.** Start a small web server on port 8000.

```bash
python3 -m http.server 8000
```

**4. Look at it working.** In a second terminal:

```bash
curl -sI localhost:8000 | head -1
```

```text
HTTP/1.0 200 OK
```

**5. Without lsof.** Try to start a second server on the same port.

```text
$ python3 -m http.server 8000
OSError: [Errno 98] Address already in use
```

The error says the port is taken. It does not say by what.

**6. With lsof.**

```text
$ lsof -i :8000
COMMAND    PID  USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
python3 232663 molef    3u  IPv4 7743610      0t0  TCP *:8000 (LISTEN)
```

![lsof output with each field numbered|600](../runs/lsof-output.png)

Ran 2026-10-01, PC (WSL, Ubuntu 24.04.2), lsof 4.95.0, by the writer in an empty folder.

**7. Clean up.** Stop the server, then check the port is free.

```text
$ kill 232663
$ lsof -i :8000
$ echo $?
1
```

No output and exit code 1 mean nothing holds the port. Run the check again after every stop: in one run the first `kill` hit the shell that started the server, and only the second `lsof` showed the server was still running.

### Reading the output

↑ [[#lsof]]

| # | Field | This run | How to read it | Backing |
|---|---|---|---|---|
| 1 | COMMAND | `python3` | the program's name, first nine characters | cited: `man lsof` |
| 2 | PID | `232663` | the [[#^def-process\|process]]'s number, what you hand to `kill` | shown |
| 3 | USER | `molef` | who owns the process | shown |
| 4 | FD | `3u` | [[#^def-fd\|file descriptor]] 3, open for reading and writing (`r` read, `w` write, `u` both) | shown and cited |
| 5 | TYPE | `IPv4` | what the descriptor points at: a socket here, `REG` for a file, `CHR` for a device | shown |
| 6 | DEVICE | `7743610` | for a socket, the kernel's number for it; `/proc/232663/fd/3` reads `socket:[7743610]` | shown |
| 7 | SIZE/OFF | `0t0` | a size or an offset; `0t` marks a decimal offset, and it means nothing for a waiting socket | stated |
| 8 | NODE | `TCP` | for a socket, the protocol; for a file, its inode number | stated |
| 9 | NAME | `*:8000 (LISTEN)` | every network address on this machine, port 8000, waiting for connections | shown |

### A second example: a client is connected

↑ [[#lsof]]

Leave the server running and hold one connection open from another program. Then look again.

```text
$ lsof -i :8000
COMMAND    PID  USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
python3 400924 molef    3u  IPv4 13172844      0t0  TCP *:8000 (LISTEN)
python3 400924 molef    4u  IPv4 13172889      0t0  TCP localhost:8000->localhost:59520 (ESTABLISHED)
python3 400944 molef    3u  IPv4 13171404      0t0  TCP localhost:59520->localhost:8000 (ESTABLISHED)

$ lsof -i :8000 -sTCP:LISTEN
COMMAND    PID  USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
python3 400924 molef    3u  IPv4 13172844      0t0  TCP *:8000 (LISTEN)

$ lsof -t -i :8000 -sTCP:LISTEN
400924
```

Ran 2026-10-03, PC (WSL, Ubuntu 24.04.2), lsof 4.95.0.

Three rows, two programs. PID 400924 is the server: one row waiting, one row for the conversation it accepted. PID 400944 is the client, holding the other end. Stopping "whatever `lsof -i :8000` shows" would stop the client as well. `-sTCP:LISTEN` keeps only the server, and `-t` prints just its PID, which is why the plans that teach this use both.

### How it works

↑ [[#lsof]]

Nothing here is derived from numbers. The mechanism, in four steps:

1. The server asks the kernel for a socket on port 8000 and gets file descriptor 3. Shown by row 6 above, and by `/proc/<PID>/fd/3` reading `socket:[7743610]`.
2. A second server asks for the same port, and the kernel refuses: `Address already in use`.
3. `lsof` reads every process's open descriptors from the kernel and prints the ones whose name matches `:8000`.
4. `kill` ends the process, the kernel closes its descriptors, and the port is free again. Shown by the empty second `lsof`.

![One process holds port 8000|700](../diagrams/lsof-01-one-process-holds-the-port.png)

### Other ways

↑ [[#lsof]]

- `ss -ltnp | grep :8000` on Linux: the same answer from the network side. Ran 2026-10-01: `LISTEN 0 5 0.0.0.0:8000 ... users:(("python3",pid=223681,fd=3))`.
- `netstat -ano | findstr :8000` on Windows: the PID is the last column. Backing: stated.
- `fuser 8000/tcp` on Linux: prints the PID only. Backing: stated.

### Taught in, applied in

↑ [[#lsof]]

**Taught in**, as `lsof -i :8000 -sTCP:LISTEN`:
- `ai-engineering/prototype-product-data-validation-end-to-end/textbook/00-the-environment.md`, line 861
- `ai-engineering/prototype-product-data-validation-end-to-end/textbook/02-design-before-code.md`, line 947
- `ai-engineering/prototype-product-data-validation-end-to-end/plans/13-reference-adk-batch-on-the-sample.md`, line 285
- `ai-engineering/prototype-product-data-validation-end-to-end/plans/28-the-batch.md`, line 199
- `ai-engineering/one-business-end-to-end/plans/12-project-app-settings-dev-server.md`, line 142, as `lsof -i :8000`

**Applied in:** nothing yet.
