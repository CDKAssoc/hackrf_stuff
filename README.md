# hackrf_stuff

This is just some stuff i have started to explore:

you should just be able to run this from a common directory
```
hackrf_sweep -f 902:928 -f 2401:2484 -f 3655:3700 -f 5170:5835 -w 200000 -r hackscanout.txt
python hackscan_parser.py
python hackrf_plotter.py
```
