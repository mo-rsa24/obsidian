# 🧭 Calling the model from a playground terminal

Everything between opening a shell in `/home/molef/playground/ai-engineering/` and a Claude API
call actually leaving the machine. It covers credentials and the failures that stop a request
before it is sent. It does not cover what the call costs or how to read `usage`, which belongs
with the cost work in
[plan 01](/home/molef/goal-setting/learning/ai-engineering/data-agents/plans/01-what-a-completion-call-costs.md).

The one system fact this file leans on: the playground is disposable and gets deleted, so nothing
here may live inside it. That is set in the environment paragraph of
[the data-agents master plan](/home/molef/goal-setting/learning/ai-engineering/data-agents/MASTER_PLAN.md).

## Table of contents

- [Words this file uses](#words-this-file-uses)
- [Before any of these](#before-any-of-these)
- [The reference block](#the-reference-block)
- [1. Make the SDK find your API key](#1-make-the-sdk-find-your-api-key)
- [If something looks wrong](#if-something-looks-wrong)
- [Where this came from](#where-this-came-from)

## Words this file uses

Navigation: 📋 [TOC](#table-of-contents) | [Next](#before-any-of-these) ➡️

- **Credential resolution**: the SDK deciding, at the moment you construct the client, which of
  several possible credentials to send. It happens in your process, before any network call.
- **`ant`**: Anthropic's command-line tool. It can store a logged-in profile on disk that the SDKs
  pick up with no environment variable set. It is not installed on this machine.

## Before any of these

Navigation: ⬅️ [Words this file uses](#words-this-file-uses) | 📋 [TOC](#table-of-contents) | [Next](#the-reference-block) ➡️

- [ ] 🖥️ **The venv is active, and the SDK is in it**
  ```bash
  python -c "import anthropic; print(anthropic.__version__)"
  ```
  ✅ **A version prints**, for example `0.100.0`. The SDK is importable, so any failure from here
  is about credentials rather than about installation.
  ❌ **`ModuleNotFoundError: No module named 'anthropic'`**: the venv is not active, or was never
  created. `source .venv/bin/activate`, then `pip install anthropic`.

## The reference block

Navigation: ⬅️ [Before any of these](#before-any-of-these) | 📋 [TOC](#table-of-contents) | [Next](#1-make-the-sdk-find-your-api-key) ➡️

Where the SDK looks for a credential, in order. First match wins, and it stops looking. This is
the table that explains why an unset `ANTHROPIC_API_KEY` is not on its own proof that you have no
credentials.

| Checked, in this order | What it is | Watch out |
|---|---|---|
| `ANTHROPIC_API_KEY` | An API key from console.anthropic.com | Set but empty still counts as set, and then the request goes out and gets a 401 rather than failing locally |
| `ANTHROPIC_AUTH_TOKEN` | A bearer token, used for OAuth flows | Wins over any profile on disk, so a stale one shadows a good login |
| The `ANTHROPIC_PROFILE` profile | A named profile written by `ant auth login` | If the named profile does not exist that is an error, not a fall-through to the next row |
| Workload identity federation env vars | Four `ANTHROPIC_*` variables set by a CI or cloud identity | Needs all four before it activates |
| The default profile on disk | `~/.config/anthropic/` | Absent on this machine, since `ant` is not installed |

## 1. Make the SDK find your API key   `unverified`

Navigation: ⬅️ [The reference block](#the-reference-block) | 📋 [TOC](#table-of-contents) | [Next](#if-something-looks-wrong) ➡️

**When you need this**

A script dies with `TypeError: Could not resolve authentication method` on the line that
constructs or first uses the client, and no request ever reached Anthropic.

**Fill in**

| What | Example | Where to get it |
|---|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-api03-xxxxxxxx` (an example, not a real key) | console.anthropic.com, Settings, then API keys, then Create key. The value is shown once and never again, so paste it somewhere before closing the dialog |

**The read-only check first**

```bash
echo "${ANTHROPIC_API_KEY:+set}${ANTHROPIC_API_KEY:-UNSET}"
```

✅ **`set`**, and the credential is already there. The failure is something else, so go to
[If something looks wrong](#if-something-looks-wrong).

❌ **`UNSET`**, which is the case this recipe is for. This form prints the word rather than the
key itself, so it is safe to run with someone looking over your shoulder.

**Set it for this shell**

```bash
export ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxx   # change this
python run.py prompt.v1.md
```

✅ **The script gets past the client construction and prints model output.** For the cost work in
plan 01 that means three SQL statements, each followed by a line like `in=214  out=31`. Two
numbers on that line is the proof: the request went out and came back billed.

❌ **`anthropic.AuthenticationError: Error code: 401`**: this is progress, not a repeat of the
same problem. The key was found and sent, and the server rejected it. See
[If something looks wrong](#if-something-looks-wrong).

**Variations**

- Check it took without printing the secret: `python -c "import os;print(len(os.environ['ANTHROPIC_API_KEY']))"`, which prints a length in the nineties.
- ⚠️ Make it survive closing the terminal, which writes your key into a file that persists. Read what is there first with `grep -n ANTHROPIC ~/.bashrc`; if that prints nothing, append with `echo 'export ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxx' >> ~/.bashrc`, then `source ~/.bashrc`. The key is then in plaintext in your home directory and in every shell you open.
- Keep it out of the shell profile: put the same `export` line in `~/.config/anthropic-key.sh` with `chmod 600`, and `source` that file when you need it.
- Never put the key in `run.py` or in the playground folder. That folder is deleted on purpose, and anything you write there is either lost or accidentally committed.

<details>
<summary><b>Why this is a TypeError and not an authentication error</b></summary>

**The failure is local, and it costs nothing**

Read the bottom of the traceback rather than the top. It ends in `_validate_headers`, called from
`_build_headers`, called from `_build_request`. The SDK was assembling the HTTP headers for the
request and found it had nothing to put in `x-api-key`, so it raised before opening a socket.

That is why the exception is a plain Python `TypeError` from the SDK's own code rather than
`anthropic.AuthenticationError`, which only exists to represent a 401 the server sent back.
Nothing was sent, nothing was billed, and no retry happened. The distinction is worth holding
onto: a local failure is free and a rejected request is not.

</details>

## If something looks wrong

Navigation: ⬅️ [1. Make the SDK find your API key](#1-make-the-sdk-find-your-api-key) | 📋 [TOC](#table-of-contents) | [Next](#where-this-came-from) ➡️

**`TypeError: Could not resolve authentication method`**: no credential was found at all. The
request was never sent. Go to [recipe 1](#1-make-the-sdk-find-your-api-key).

**`anthropic.AuthenticationError`, code 401**: a credential was found and the server rejected it.
Different problem. The usual causes are a key that was revoked, a key copied with a trailing
newline or a leading space, or a key from a different organisation. Re-check with
`python -c "import os;print(repr(os.environ['ANTHROPIC_API_KEY'][-4:]))"` and compare the last four
characters against the console.

**It worked in one terminal and not another**: `export` applies to the shell you typed it in and
its children, and nothing else. A second terminal, a new VS Code panel, or a `sudo` command all
start clean. Use the shell-profile variation in recipe 1 if this keeps happening.

**`NameError` or a missing module after everything above passed**: you are in a different venv
from the one the SDK was installed into. `which python` should print a path under
`.venv/bin/` inside the folder you are working in.

## Where this came from

Navigation: ⬅️ [If something looks wrong](#if-something-looks-wrong) | 📋 [TOC](#table-of-contents)

| What | How it was established | When |
|---|---|---|
| The traceback ends in `_validate_headers`, so no request is sent | Read off the real traceback from `python run.py prompt.v1.md` in the playground | 2026-09-08 |
| `anthropic` 0.100.0 is importable in the playground venv | `python3 -c "import anthropic; print(anthropic.__version__)"` | 2026-09-08 |
| `ANTHROPIC_API_KEY` is unset and `ant` is not installed on this machine | `env` filtered for `ANTHROPIC` returned nothing; `which ant` returned nothing | 2026-09-08 |
| The credential resolution order | The `claude-api` skill's authentication reference, not run | 2026-09-08 |
| Everything in recipe 1 downstream of the read-only check | Written from that reference. No key exists yet, so nothing past the check has been run | 2026-09-08 |
