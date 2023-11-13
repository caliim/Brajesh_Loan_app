import pickle

with open("./artefacts/classifier.pkl", 'rb') as file:
    clf = pickle.load(file)

print(clf)
