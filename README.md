# The World in One Page — Sunday, November 22, 2026

One image that sums up a whole day of world news: the front page of
an imaginary Sunday newspaper dated **Sunday, 22 November 2026**,
drawn at 1024x1024 so the date and every headline stay readable even
when the picture is shrunk to a thumbnail. This completed-day
edition carries **36 stories from 6 continents**: a lead report, a
dotted world map whose numbered pins match the stories, 35 numbered
briefs in three columns, and a sources line along the foot of the
page.

This repository is an entry in the make.fun competition
[Sum up 22 November's world news in one image](https://make.fun/c/news-image-20261122).

![make.fun competition](https://make.fun/badge/news-image-20261122.svg)
![rank](https://make.fun/badge/news-image-20261122/hmnk0311/news-image-20261122/rank.svg)
![reward](https://make.fun/badge/news-image-20261122/hmnk0311/news-image-20261122/reward.svg)

## What the front page reports

The lead is the day's biggest story: **COP31 collapsed without a
deal**. Nearly 200 nations failed over fossil fuels in Antalya —
the EU rejected a text that named none, the $120 billion adaptation
goal was dropped, and the longest climate summit on record ended in
the first such failure since Copenhagen in 2009.

Around it, the 35 numbered briefs cover the rest of the Sunday:
NATO's vow to defend every inch of Poland and Russian strikes on
Sloviansk; France's sixth protest weekend, a Brexit row in London
and a rejected EU budget; Liverpool's 4-0 rout of Manchester
United, Barcelona's comeback and Alcaraz's ATP Finals crown; a
Houthi missile intercepted over the Red Sea and Iran's terms for
reopening Hormuz; Shuri Castle restored in Naha, a sumo title in
Fukuoka and a snowbound Fukushima village reconnected; a factory
fire in Indonesia, mass food poisoning in India, floods in
Selangor, Nepal's prime minister in Delhi, China's second cruise
ship and a Singapore film's Golden Horse double; a capsized
funeral boat in Nigeria, a Russian corvette sunk by sea drones in
Benghazi and drones over Khartoum; the capture of an FBI
most-wanted cartel boss in Mexico, another FBI database breach,
a promised 10% cap on card interest, an abolish-ICE call in
Seattle, Verstappen's Las Vegas win and Kansas City's first NWSL
title; a town levelled by a Brazilian supercell and Boca Juniors'
Copa Sudamericana; and in Oceania a record Indian Test total in
Wellington, a Pacific rugby sweep led by Fiji, Brisbane's upset
of Sydney in the NBL, and a weakening cyclone in the Cook Islands.

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
