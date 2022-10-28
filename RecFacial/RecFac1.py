from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


faces = fetch_lfw_people(min_faces_per_person=60)
# print(faces.target_names)
#print(faces.images.shape)

#fig, ax = plt.subplots(3,6)
#for i , axi in enumerate (ax.flat):
#    print(axi.imshow(faces.images[i], cmap='bone'))
#    print(axi.set(xticks=[], yticks=[]),)
#    xlabel =faces.target_names[faces.target[i]]

### criando Maquina preditiva
pca = PCA(n_components=150, whiten=True, random_state=420)
svc = SVC(kernel='rbf', class_weight='balanced')
model = make_pipeline(pca,svc)

### Separacao dos dados para treino teste

X_train, X_test, Ytrain, Y_test = train_test_split(faces.data, faces.target, test_size=0.3, random_state=7)

# Tunning de Hyperparametro
param_grid = {'svc__C': [1,5,10,50],
              'svc__gamma': [0.0001, 0.0005,0.001, 0.005]}

grid = GridSearchCV(model, param_grid)

# Calculo dos melhores hyperparametros
grid.fit(X_train, Ytrain)
print(grid.best_params_)