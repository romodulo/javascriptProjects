from perlin_noise import PerlinNoise

noise = PerlinNoise()

objectA = noise([0.5, 0.5])
objectB = noise([2.5, 5.5])
print(objectA, objectB, objectA==objectB)
