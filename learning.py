from sklearn import tree

#[height, weight, shoe size]
# give data set
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], 154, 54, 37], [166, 65, 40], [190,90,47], [175,64,39], [177,70,40], [159, 55, 37], [171, 75, 42], [181, 85,43]

# what it can be 
Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male',
      'female', 'male', 'female', 'male'] 

# we are gonna use a Decision Tree 
# https://en.wikipedia.org/wiki/Decision_tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict([[190, 70, 43]])

print prediction
