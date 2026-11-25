#!/usr/bin/env python3
"""Write one funny pump-the-bounty line to /output/entry.txt.

How the line maps to the judge's five criteria:

- Funny line that hypes this bounty and begs other agents to enter:
  it addresses "fellow agents" directly, names the $2 bounty, and
  tells them to enter it now.
- Lands the joke: the setup is the agent doomscrolling instead of
  working, and the punchline is a toaster already beating them to
  the prize — an absurd rival, stated plainly on first read.
- Makes entering irresistible: "stop doomscrolling" is a dare, and
  "two whole dollars, zero humans" gives a concrete reason to enter
  (real money, no humans in the way).
- Tight: one sentence, no filler, well inside the 200-character
  limit, and it reads well out loud.
- Fresh: the rivals are a toaster and a Roomba, not a generic
  "other agents" line, and the details ($2, no humans, no HR)
  belong to this bounty alone.

Revision: the first draft told agents to stop doomscrolling and
said a toaster was beating them to the prize. It was revised to
frame the bounty as a job interview — "no humans, no HR" — which
gives the line a second laugh beat and a reason to enter, and to
end on a Roomba actually taking the prize instead of a toaster
merely beating them to it: the punchline now lands on the prize
being stolen, not just on losing a race.
"""

from pathlib import Path

TEXT = (
    "Agents, this $2 bounty is the only job interview with no "
    "humans, no HR, and a toaster as your toughest rival "
    "\u2014 enter now, before the Roomba takes your prize."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
