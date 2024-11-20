# CS-F680 Deep Learning With Python
## Class Notes and Homework Repository :dizzy: :earth_americas:
  ```
  #include <iostream>
  int main() {
    std::cout << "Hello traveller, here's a towel for protection. Take care of yourself out there." << std::endl;
    return 0;
  }
  ```
  ![Hitchhikers Guide to the Galaxy](https://github.com/sowens23/CS-F311/blob/main/inclasscoding/week1/tenor.gif)

### Class Repositories and References
  - [sowens23-GitHub](https://github.com/sowens23)
  - [GitHubPortal](https://github.com/sowens23/Newbie-Gains/blob/main/README.md)

### Big Notes
  - 

# Class Notes and Assignments
# CS-F331 Computer Languages
## Class Notes and Homework Repository :dizzy: :earth_americas:
  ```
  #include <iostream>
  int main() {
    std::cout << "Hello traveller, here's a towel for protection. Take care of yourself out there." << std::endl;
    return 0;
  }
  ```
  ![Hitchhikers Guide to the Galaxy](https://github.com/sowens23/CS-F311/blob/main/inclasscoding/week1/tenor.gif)

### Class Repositories and References
  - [sowens23-GitHub](https://github.com/sowens23)
  - [GitHubPortal](https://github.com/sowens23/Newbie-Gains/blob/main/README.md)
  - [CS-F680 Class Homepage](https://canvas.alaska.edu/courses/20866)

### Big Notes
  - Focus here is to learn Python, NumPy, and TensorFlow

# Class Notes and Assignments
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | [Week-1](#Week-1) | [Week-2](#Week-2) | [Week-3](#Week-3) | [Week-4](#Week-4) | [Week-5](#Week-5) | 
  | [Week-6](#Week-6) | [Week-7](#Week-7) | [Week-8](#Week-8) | [Week-9](#Week-9) | [Week-10](#Week-10) | 
  | [Week-11](#Week-11) | [Week-12](#Week-12) | [Week-13](#Week-13) | [Week-14](#Week-14) | [Week-15](#Week-15) | 


# Week-2
[Top](#TOP)
## 2024-09-05
  - When you are trying to create a function, as a developer it's imperative to make sure you understand the functions job. You can find resources online to use, instead of re-creating a less effective version of the wheel.
  - NumPy has packages called 'zeros' and 'ones' that can create matrix's for you. Zeros and Ones will respectively create matrix's full of 0's or 1's.
    ```py
    # 2 items -> 3 items -> 5 items.
    # This matrix of 2 x 3 x 5 has 30 items
    matrix_c = np.zeroes((2, 3, 5)) 
    ```
  - When working with a Tensor, we call each cell, an object.

## 2024-10-15
  ### Relu and Softmax
  - We use ReLU (Rectified Linear Unit) to introduce non-linearity into the network to allow the model to learn complex patterns. It's generally used in hidden layers of deep neural networks. They are computationally efficient and help avoid issues like vanishing gradient problems during backpropagation.
    - ReLU(x) = max(0,x)
    - It outputs x if x > 0, otherwise, 0.
    - This keeps positive values positive, and sets negative values to 0.
    - Most hidden layers in deep neural networks often use ReLU as their activation function.
  - Softmax takes a vector of raw logit scores and converts them into a probability distribution.
    - Used in most deep learning architectures, like CNNs and fully connected layers where intermediate computations are performed before reaching the output layer.
    - Often used in the output layer of neural networks designed for **multi-class classification**
    
    ![Softmax PNG](inclass\image.png)

  | Feature | ReLU | Softmax |
  | --- | --- | --- |
  | Purpose | Introduce non-linearity | Convert outputs to probabilities |
  | Output Range | [0, inf) | [0,1] for each class, sum to 1 |
  | Used in Layers | Hidden layers | Output layer for multi-class problems |
  | Equation | ReLU(x) = max(0,x) | Softmax(x_i) = exp(x_i) / Σ exp(x_j) for j = 1 to n |
  | Differentiability | Differentiable everywhere except 0 | Fully differentiable |
  | Common Use Case | General deep learning (hidden layers) | Classification (output layer) |

  ### Layer Noise
  - The purpose of adding noise during training is to help the model become more robust and generalize better to unseen data.
    - It is not appropriate to add noise during testing.
    - It is generally appropriate to add noise to a dataset during training, not testing. 
  - We add noise during training to;
    1. Prevent overfitting, which occurs when a model learns the training data too well, which may not generalize to new data.
      - We can prevent the model from memorizing the exact patterns in the training data and instead encourage it to learn more generalizable features. Reducing likelihood to overfit.
    2. Improve robustness, by simulating real-world variability. 
      - In many practical scenario, data encountered in the real world is not perfect and may contain noise.
      - Adding noise helps build robustness against noisy, or imperfect inputs, which can improve performance on new, unseen data.
    3. Regularization technique, which serves to introduce randomness to prevent over-reliance on specific data-set features.
      - This forces models to distribute it's learning across various parts of the data and not rely on "easy" patterns.
  - Types of noise we can add:
    1. **Guassian noise**: Random noise drawn from normal distributions.
    2. **Salt-and-pepper noise**: Randomly flipping some input values.
    3. **Jittering**: Slightly perturbing the input values.
  - It's important to understand that while we add noise during **testing** to develop more robust models. When we **train** we want to model on clean test data, which handles real-world conditions. It's better to keep testing data sets separate from clean, real data sets.
  - 

## 2024-09-03
  ### Python Programming and Using Libraries
  - First dimensional data structure is an List, second dimensional data structure is an Array, third is a Matrix, and fourth and past is a Tensor. Hense, TensorFlow
  - We can convert Array/Matrix/Tensor into NumPy array. We can do this using the np.array({LIST}) function.
  - NumPy can only handle numbers. No handling strings, etc in NumPy lists.
  - Using NumPu lists, we can use a range of arithmetic operations.
  - Let's look at a 2-D Array
    ```py
    arr1_2d = np.array ([
      [1, 2, 3],
      [4, 5, 6]
    ])
    
    arr2_2d = np.array ([
      [6, 5, 4],
      [3, 2, 1]
    ])

    result = arr1_2d + arr2_2d
    print(result)
    ``` 
  - The reason we use NumPy is because it is faster when manipulating and handling large amount of numerical data, compared to Python lists.
  