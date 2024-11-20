import tensorflow as tf
import numpy as np
import pandas as pd

#(1pt) ToDo: Modify the code here to read the I2 and I3 column of the dataset of the as inputs

df = pd.read_csv('WisconsinBreastCancerDataSet.csv')

num_samples_per_class = 1000
negative_samples = np.random.multivariate_normal(
    mean=[0, 3],
    cov=[[1, 0.5],[0.5, 1]],
    size=num_samples_per_class)
positive_samples = np.random.multivariate_normal(
    mean=[3, 0],
    cov=[[1, 0.5],[0.5, 1]],
    size=num_samples_per_class)

inputs = df[['I2', 'I3']].values.astype(np.float32)
inputs


#(3pts) ToDo: Modify the code here to read the 'O' column of the dataset as targets.
# 'O' column contains non-numeric data 'M' and 'B'.
# So, you need to first convert them to numeric data (M to 1, b to 0, or the other way)
# (You can get the code for such conrsion in Neural_Network_with_Scikit_learn.ipynb that we discussed in class.)
# Then, covert that numeric data in targets.

df['O_numeric'] = df['O'].map({'M': 1, 'B': 0})

targets = df[['O_numeric']].values.astype(np.float32)
targets = targets.reshape(-1,1)
targets


#Do not change anything here
input_dim = 2
output_dim = 1
W = tf.Variable(initial_value=tf.random.uniform(shape=(input_dim, output_dim)))
b = tf.Variable(initial_value=tf.zeros(shape=(output_dim,)))


#Do not change anything here
def model(inputs):
    L1 = tf.matmul(inputs, W) + b
    return L1

#Do not change anything here
def square_loss(targets, predictions):
    per_sample_losses = tf.square(targets - predictions)
    return tf.reduce_mean(per_sample_losses)


#Do not change anything here
learning_rate = 0.1

def training_step(inputs, targets):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = square_loss(targets, predictions)
    grad_loss_wrt_W, grad_loss_wrt_b = tape.gradient(loss, [W, b])
    W.assign_sub(grad_loss_wrt_W * learning_rate)
    b.assign_sub(grad_loss_wrt_b * learning_rate)
    return loss


#(0.5pts) ToDo: Modify the code here to store the loss of each step in an array
losses = []

for step in range(50):
    loss = training_step(inputs, targets)
    print(f"Loss at step {step}: {loss:.4f}")


#(2.5) ToDo: Write the code to plot the Loss function

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.plot(losses, label='Training Loss')
plt.title('Training Loss')
plt.xlabel('Steps')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.show()

#(10pts) ToDO: Create a new neural network with the following architecture:
# One input layer, three hidden layers (layer0, layer1, layer2), and one output layer
input_size = 2 # Inputs: I2, I3
layer0_size = 2
layer1_size = 3
layer2_size = 2
output_neurons = 1

# Initialize the weights and biases for each layer
W0 = tf.Variable(tf.random.normal([input_size, layer0_size]), dtype=tf.float32)
b0 = tf.Variable(tf.zeros([layer0_size]), dtype=tf.float32)

W1 = tf.Variable(tf.random.normal([layer0_size, layer1_size]), dtype=tf.float32)
b1 = tf.Variable(tf.zeros([layer1_size]), dtype=tf.float32)

W2 = tf.Variable(tf.random.normal([layer1_size, layer2_size]), dtype=tf.float32)
b2 = tf.Variable(tf.zeros([layer2_size]), dtype=tf.float32)

W_out = tf.Variable(tf.random.normal([layer2_size, output_neurons]), dtype=tf.float32)
b_out = tf.Variable(tf.zeros([output_neurons]), dtype=tf.float32)

# Define ReLU activation function
def relu(x):
    return tf.maximum(0, x)

# Define the forward pass function
def forward_pass(inputs):
    # Layer 0
    layer0_output = relu(tf.matmul(inputs, W0) + b0)
    
    # Layer 1
    layer1_output = relu(tf.matmul(layer0_output, W1) + b1)
    
    # Layer 2
    layer2_output = relu(tf.matmul(layer1_output, W2) + b2)
    
    # Output layer (no activation)
    output = tf.matmul(layer2_output, W_out) + b_out
    return output

# Define the MSE loss function
def mse_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Training step
learning_rate = 0.01
def training_step(inputs, targets):
    with tf.GradientTape() as tape:
        predictions = forward_pass(inputs)
        loss = mse_loss(targets, predictions)
    gradients = tape.gradient(loss, [W0, b0, W1, b1, W2, b2, W_out, b_out])
    
    W0.assign_sub(learning_rate * gradients[0])
    b0.assign_sub(learning_rate * gradients[1])
    W1.assign_sub(learning_rate * gradients[2])
    b1.assign_sub(learning_rate * gradients[3])
    W2.assign_sub(learning_rate * gradients[4])
    b2.assign_sub(learning_rate * gradients[5])
    W_out.assign_sub(learning_rate * gradients[6])
    b_out.assign_sub(learning_rate * gradients[7])
    
    return loss

# Store the loss values for plotting
losses = []

# Train the neural network
epochs = 50
for step in range(epochs):
    loss = training_step(inputs, targets)
    losses.append(loss)
    print(f"Loss at step {step}: {loss:.4f}")

#(2.5pts) Plot the Loss function
plt.figure(figsize=(8, 6))
plt.plot(losses, label='Training Loss')
plt.title('Training Loss over Time')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.show()