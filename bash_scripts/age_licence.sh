#!/bin/bash

awk -F',' '
  BEGIN { age = 25; }
  NR==1 { next; }
  {
    if ($2 < age) {
      if ($4 == "yes") under_licence++;
      else if ($4 == "no") under_nolicence++;
      else under_undefined++;
    } else {
      if ($4 == "yes") over_licence++;
      else if ($4 == "no") over_nolicence++;
      else over_undefined++;
    }
  }
  END {
    print "Under 25 without licence: ", under_nolicence/15
    print "Under 25 with licence: ", under_licence/15
    if (under_undefined > 0)
      print "Under 25 undefined: ", under_undefined/15
    print "Over 25 without licence: ", over_nolicence/15
    print "Over 25 with licence: ", over_licence/15
    if (over_undefined > 0)
      print "Over 25 undefined: ", over_undefined/15
  }' data/log.csv
