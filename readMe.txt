Perceptron algorithm

Didn't really wanna learn python libraries for making images, so I just made every image 1s and 0s, which is probably
dumb but whatever. The algorithm starts w/ starting weights, then adjusts those weights to make weights.txt, then
makes those weights look nicer w/ finalweights.txt. trainer.py uses the standard perceptron algorithm, by making a
guess and then adjusting the weights accordingly. The activation value is simply a dot product of the values from
weights.txt and the image file. If the activation is >= the bias value, which is just another value in the weights.txt
file, it'll guess 1. Otherwise it'll guess 0. If it guesses wrong, it will add or subtract the image vector from the
weight vector. It'll keep repeating this process until it guesses every image correctly.