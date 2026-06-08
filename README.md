
# Miasma Sample

This repository contains a safe variant of the Miasma worm, as a sample
without the dropper payload itself to be able to test it safely against
SIEM/SOAR rulesets.

As it does not contain an actual worm implant, the [.github/setup.js](/.github/setup.js)
file has been replaced with an empty file that does nothing and contains
only a comment.

This repository is used as a true positive test case for the
[antimiasma](https://github.com/cookiengineer/antimiasma.git) tool.


### License

AGPL-3.0

