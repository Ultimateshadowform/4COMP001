# Developer checks

Checks I ran in the terminal while building each part, before committing.
Archie's automated tests are in `tests/` and Vlad's manual tests are in `docs/testing`.

## Card 11: storage.py (25th November 2026)

Tested with a test user, oliver01, and a test file, `try.json`, which I deleted afterwards.

| # | What I checked | What should happen | Result |
|---|---|---|---|
| 1 | `load_data` when there is no file yet | Gives back `{}` | Pass |
| 2 | `get_user` for a user who doesn't exist | Gives back `None` (nothing is shown) | Pass |
| 3 | `create_account` for oliver01 | Saves the user with a weekly budget of 0 and no spending | Pass |
| 4 | `set_budget` to 60 | `get_user` now shows a weekly budget of 60 | Pass |
| 5 | `add_spending` twice (£4.50 Food with the note " Meal deal ", then £2 Transport) | Two entries with ids 1 and 2, the dates saved as text, and the note trimmed to "Meal deal" | Pass |
| 6 | `delete_spending` entry 1 | Gives back `True` | Pass |
| 7 | `delete_spending` entry 1 again | Gives back `False`, because it has already gone | Pass |
| 8 | `add_spending` after the delete (£3 Other, "Pens") | The new entry gets id 3, not 2 (last id + 1), so ids never repeat | Pass |

Screenshot: `screenshots/card-11-storage-check.png`

Ruff (`python -m ruff check`): all checks passed.
