#!/bin/sh
mkdir -p ./console_output/
echo $(date -u) "***hello***" | tee -a ./console_output/screen.out
python exampleM1.py -in ./data_jpg/ -f *.jpg -n LeninGF -ot | tee -a ./console_output/screen.out
python exampleM1.py -in ./data_jpg/ -f *.jpg -n KenshinHimura  | tee -a ./console_output/screen.out

