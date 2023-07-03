'''
/**
* @author Karine Mendes Tavares
*/
'''

import pandas as pd
import matplotlib.pyplot as plt
import glob

# Set the figure size
plt.rcParams["figure.figsize"] = [10.00, 4.50]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns
columns = [ 'train_accuracy', 'val_accuracy']

# fig, (ax1, ax2) = plt.subplots(1, 2)
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, sharey=ax1)
fig.suptitle('DenseNet-121', fontsize=15)

# DenseNet121
# InceptionResNetV2

# densenet
# IRV2

# Get CSV files list from a folder
path = "K:/Faculdade/TCC/main/loss/10fold/densenet/imagenet"
csv_files = glob.glob(path + "/*.csv")

train_accuracy_sum = [0] * 50
val_accuracy_sum = [0] * 50
for index, file in enumerate(csv_files):
    df = pd.read_csv(file, usecols=columns)
    for index, train_accuracy in enumerate(df['train_accuracy']):
        train_accuracy_sum[index] += train_accuracy
        val_accuracy_sum[index] += df['val_accuracy'][index]

train_accuracy_mean = []
val_accuracy_mean = []
for i in range(0,50):
    train_accuracy_mean.append(train_accuracy_sum[i]/10)
    val_accuracy_mean.append(val_accuracy_sum[i]/10)

epochs = list(range(1,51))
ax1.plot(epochs,train_accuracy_mean, label='treino', marker = '.')
ax1.legend(loc="center right")
ax1.plot(epochs,val_accuracy_mean, label='validação', marker = '.')
ax1.legend(loc="center right")
ax1.set_xlabel("Épocas") 
ax1.set_ylabel("Acurácia")
ax1.title.set_text('Imagenet')

# Get CSV files list from a folder
path = "K:/Faculdade/TCC/main/loss/10fold/densenet/radimagenet"
csv_files = glob.glob(path + "/*.csv")

train_accuracy_sum = [0] * 50
val_accuracy_sum = [0] * 50
for index, file in enumerate(csv_files):
    df = pd.read_csv(file, usecols=columns)
    for index, train_accuracy in enumerate(df['train_accuracy']):
        train_accuracy_sum[index] += train_accuracy
        val_accuracy_sum[index] += df['val_accuracy'][index]

train_accuracy_mean = []
val_accuracy_mean = []
for i in range(0,50):
    train_accuracy_mean.append(train_accuracy_sum[i]/10)
    val_accuracy_mean.append(val_accuracy_sum[i]/10)

epochs = list(range(1,51))
ax2.plot(epochs,train_accuracy_mean, label='treino', marker = '.')
ax2.legend(loc="center right")
ax2.plot(epochs,val_accuracy_mean, label='validação', marker = '.')
ax2.legend(loc="center right")
ax2.set_xlabel("Épocas") 
ax2.set_ylabel("Acurácia")
ax2.title.set_text('RadImagenet')
plt.show()
