# interactive-sumo-exporter

## CLI -> SUMO
```
python3 run.py -i cli -o OUTPUT_NAME
```
The interactive CLI-Importer starts. Aferwards the export begins.

## PlanPro -> SUMO
```
python3 run.py -i planpro -f PLANPRO_FILENAME -o OUTPUT_NAME
```

## ORM -> SUMO
```
python3 run.py -i orm -o OUTPUT_NAME
```
A Browser window opens. Afer clicking on `Submit polygon` the export begins.

## Output
The output can be found in `sumo-config`.<br>
`-o OUTPUT_NAME` is optional. The default name is `output`.
