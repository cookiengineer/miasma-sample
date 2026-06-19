
# Miasma Sample

This repository contains safe samples of the Miasma worm. These samples
don't contain the dropper payload itself and are used actively for
testing in SIEM/SOAR environments.

As it does not contain an actual worm implant, the `.github/setup.js`
and `_index.js` files have been replaced with an empty file that do
nothing and contain only a comment.

Because the Miasma worm campaigns are an actively evolving threat,
relevant changes to the campaigns are stored in different subfolders,
showing how exactly the implant dropper mechanisms change over time.

- [01-blight-campaign](./01-blight-campaign) "Miasma" campaign sample, targeting Node.js (NPM) and AI-assisted IDEs
- [02-hades-campaign](./02-hades-campaign) "Hades" campaign sample, targeting Python (PyPi)
- [03-hades-campaign](./03-hades-campaign) "Hades" campaign sample, targeting PHP (Composer)
- [04-atomic-campaign](./04-atomic-campaign) "Atomic Arch" campaign sample, targeting AUR and Pacman


This repository is used as a true positive test case for the
[antimiasma](https://github.com/cookiengineer/antimiasma.git) tool.


### License

AGPL-3.0

