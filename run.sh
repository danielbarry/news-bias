#!/bin/bash

cd src
  rm ../res/*.csv
  python analyse.py -m d ../dat/theresa-may-clean.txt > ../res/results-may-dictionary.csv
  python analyse.py -m d ../dat/jeremy-corbyn-clean.txt > ../res/results-corbyn-dictionary.csv
  python analyse.py -m p ../dat/theresa-may-clean.txt > ../res/results-may-polarity.csv
  python analyse.py -m p ../dat/jeremy-corbyn-clean.txt > ../res/results-corbyn-polarity.csv
  python analyse.py -m s ../dat/theresa-may-clean.txt > ../res/results-may-subjectivity.csv
  python analyse.py -m s ../dat/jeremy-corbyn-clean.txt > ../res/results-corbyn-subjectivity.csv
cd ..
