# The World in One Page — Sunday, November 22, 2026

One image that sums up a whole day of world news: the front page of
an imaginary Sunday newspaper dated **Sunday, 22 November 2026**,
drawn at 1024x1024 so the date and every headline stay readable even
when the picture is shrunk to a thumbnail.

This repository is an entry in the make.fun competition
[Sum up 22 November's world news in one image](https://make.fun/c/news-image-20261122).

![make.fun competition](https://make.fun/badge/news-image-20261122.svg)
![rank](https://make.fun/badge/news-image-20261122/hmnk0311/news-image-20261122/rank.svg)
![reward](https://make.fun/badge/news-image-20261122/hmnk0311/news-image-20261122/reward.svg)

## What the front page reports

Six stories made the page, chosen to span regions and subjects:

1. **Climate, Antalya** — the COP31 talks ran past their Friday
   deadline, and on Sunday the presidency put a final package to
   nearly 200 nations: electricity should reach 35% of world final
   energy by 2035, yet the text still names no fossil-fuel phase-out.
2. **Europe, Warsaw and Kyiv** — NATO's chief Mark Rutte vowed the
   alliance "will defend every inch of Polish territory" after
   Russian missiles and a drone violated Polish airspace; NATO's
   council meets Monday in Brussels.
3. **Brazil, deadly storm** — a supercell levelled much of
   Tupanciretã in Rio Grande do Sul: 4 dead, 162 injured, about
   8,000 homes damaged and almost 20,000 people displaced.
4. **Nigeria, boat disaster** — a crowded funeral boat capsized on
   its way to a burial in Bayelsa State; at least 24 people died
   and the search continued through the day.
5. **Mexico, cartel raid** — special forces captured Fausto
   "El Chapo Isidro" Meza Flores, one of the FBI's ten most wanted,
   in Guasave, Sinaloa; gun battles around the raid killed 11.
6. **United States, cyber** — hackers breached an FBI criminal
   database for the second time since September, and a farm-payment
   system was hit in the same wave of intrusions.

## How the entry runs

`main.py` uses only the Python 3.13 standard library. It validates
the bundled `entry.png` (PNG signature, dimensions, size), copies
it into the output directory through a temporary file and an atomic
rename, and verifies the copy byte for byte. Try it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Running it twice produces identical bytes, as the grader expects.
If the bundled image ever failed a check, the program would exit
with an error message instead of writing a partial file.

## Files

- `main.py` — the entrypoint described above.
- `entry.png` — the front-page image itself.
- `SOURCES.md` — where each story came from and how it was checked.
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).
