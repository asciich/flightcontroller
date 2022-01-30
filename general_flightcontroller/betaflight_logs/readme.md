# Betaflight logs

## Installation

On arch linux install the `blackbox-tools` package:

```bash
yay -S blackbox-tools
```

## Decode logs

Decoding logs will write gps files and csv files:

```bash
blackbox_decode *.BFL
```

##  Render as vide

## Only render sticks in the bottom middle at 25 Fps:

```
blackbox_render \
    --fps 25 \
    --no-draw-pid-table \
    --no-draw-craft \
    --draw-sticks \
    --no-draw-time \
    --no-draw-acc \
    --no-plot-motor \
    --no-plot-pid \
    --no-plot-gyro \
    --sticks-top 800 \
    --sticks-right 960 \
    --sticks-width 50 \
    *.BFL
```

